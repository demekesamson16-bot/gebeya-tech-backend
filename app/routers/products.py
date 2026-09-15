from typing import Optional

from fastapi import APIRouter, Depends, Header, HTTPException, Query
from sqlalchemy import func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..auth import get_current_user, is_admin
from ..database import get_db
from ..models import Category, Product
from ..schemas import CategoryOut, ProductIn, ProductOut, ProductUpdate

router = APIRouter(prefix="/api", tags=["catalog"])


@router.get("/products", response_model=list[ProductOut])
async def list_products(
    q: Optional[str] = None,
    category: Optional[str] = None,
    brand: Optional[str] = None,
    storage: Optional[str] = None,
    ram: Optional[str] = None,
    condition: Optional[str] = None,
    location: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    limit: int = Query(200, le=500),
    offset: int = 0,
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Product).where(Product.is_active == True)

    if q:
        stmt = stmt.where(
            or_(
                Product.name.ilike(f"%{q}%"),
                Product.description.ilike(f"%{q}%"),
            )
        )

    if category:
        stmt = stmt.join(Category).where(Category.slug == category)

    if min_price is not None:
        stmt = stmt.where(Product.price >= min_price)
    if max_price is not None:
        stmt = stmt.where(Product.price <= max_price)

    def spec_match(key: str, value: str):
        return func.json_extract(Product.specs, f"$.{key}") == value

    if brand:
        stmt = stmt.where(spec_match("brand", brand))
    if storage:
        stmt = stmt.where(spec_match("storage", storage))
    if ram:
        stmt = stmt.where(spec_match("ram", ram))
    if condition:
        stmt = stmt.where(spec_match("condition", condition))
    if location:
        stmt = stmt.where(
            func.json_extract(Product.specs, "$.location").ilike(f"%{location}%")
        )

    stmt = stmt.order_by(Product.created_at.desc()).offset(offset).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.get("/products/{product_id}", response_model=ProductOut)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/categories", response_model=list[CategoryOut])
async def list_categories(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Category).order_by(Category.name))
    return result.scalars().all()


@router.post("/products", response_model=ProductOut)
async def create_product(
    payload: ProductIn,
    x_init_data: str = Header(default=""),
    db: AsyncSession = Depends(get_db),
):
    user = get_current_user(x_init_data)
    if not is_admin(user["id"]):
        raise HTTPException(status_code=403, detail="Admin only")

    product = Product(**payload.model_dump())
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


@router.put("/products/{product_id}", response_model=ProductOut)
async def update_product(
    product_id: int,
    payload: ProductUpdate,
    x_init_data: str = Header(default=""),
    db: AsyncSession = Depends(get_db),
):
    user = get_current_user(x_init_data)
    if not is_admin(user["id"]):
        raise HTTPException(status_code=403, detail="Admin only")

    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    await db.commit()
    await db.refresh(product)
    return product


@router.delete("/products/{product_id}")
async def delete_product(
    product_id: int,
    x_init_data: str = Header(default=""),
    db: AsyncSession = Depends(get_db),
):
    user = get_current_user(x_init_data)
    if not is_admin(user["id"]):
        raise HTTPException(status_code=403, detail="Admin only")

    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.is_active = False
    await db.commit()
    return {"ok": True}


@router.get("/filters/{category_slug}")
async def get_category_filters(
    category_slug: str,
    db: AsyncSession = Depends(get_db),
):
    """Return available filter options + counts for a category."""
    stmt = (
        select(Product)
        .join(Category)
        .where(Product.is_active == True)
        .where(Category.slug == category_slug)
    )
    result = await db.execute(stmt)
    products = result.scalars().all()

    brands: dict = {}
    storages: dict = {}
    rams: dict = {}
    conditions: dict = {}
    locations: dict = {}
    types: dict = {}

    for p in products:
        s = p.specs or {}
        if s.get("brand"):
            brands[s["brand"]] = brands.get(s["brand"], 0) + 1
        if s.get("storage"):
            storages[s["storage"]] = storages.get(s["storage"], 0) + 1
        if s.get("ram"):
            rams[s["ram"]] = rams.get(s["ram"], 0) + 1
        if s.get("condition"):
            conditions[s["condition"]] = conditions.get(s["condition"], 0) + 1
        if s.get("location"):
            locations[s["location"]] = locations.get(s["location"], 0) + 1
        if s.get("type"):
            types[s["type"]] = types.get(s["type"], 0) + 1

    return {
        "brand": brands,
        "storage": storages,
        "ram": rams,
        "condition": conditions,
        "location": locations,
        "type": types,
        "total": len(products),
    }
