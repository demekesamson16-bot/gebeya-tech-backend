from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..models import PhoneSpec
from ..schemas import PhoneSpecOut

router = APIRouter(prefix="/api/phones", tags=["phones"])


@router.get("", response_model=list[PhoneSpecOut])
async def list_phones(
    brand: str | None = None,
    year_from: int = Query(2000),
    q: str | None = None,
    limit: int = Query(200, le=500),
    db: AsyncSession = Depends(get_db),
):
    """List phones for the compare picker.
    - Filter by `brand` (e.g. Apple, Samsung)
    - Filter by `year_from` (default 2000)
    - Search by `q` (matches model or brand name)
    """
    stmt = select(PhoneSpec).where(PhoneSpec.release_year >= year_from)
    if brand:
        stmt = stmt.where(PhoneSpec.brand == brand)
    if q:
        stmt = stmt.where(
            or_(PhoneSpec.model.ilike(f"%{q}%"), PhoneSpec.brand.ilike(f"%{q}%"))
        )
    stmt = stmt.order_by(PhoneSpec.brand, PhoneSpec.release_year.desc()).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.get("/brands")
async def list_brands(db: AsyncSession = Depends(get_db)):
    """Returns unique brand names for the filter chips."""
    result = await db.execute(
        select(PhoneSpec.brand).distinct().order_by(PhoneSpec.brand)
    )
    return [r[0] for r in result.all()]


@router.get("/compare", response_model=list[PhoneSpecOut])
async def compare_phones(ids: str, db: AsyncSession = Depends(get_db)):
    """Fetch 2 (or more) phones by ID for side-by-side comparison.
    Example: /api/phones/compare?ids=1,5
    """
    try:
        id_list = [int(x.strip()) for x in ids.split(",") if x.strip()]
    except ValueError:
        raise HTTPException(400, "Invalid ids format. Use comma-separated integers.")

    if len(id_list) < 2:
        raise HTTPException(400, "Provide at least 2 phone ids.")

    result = await db.execute(select(PhoneSpec).where(PhoneSpec.id.in_(id_list)))
    return result.scalars().all()