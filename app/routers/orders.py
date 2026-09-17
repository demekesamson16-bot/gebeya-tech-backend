<<<<<<< HEAD
from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..auth import get_current_user, is_admin
from ..bot import bot
from ..config import settings
from ..database import get_db
from ..models import Order, OrderItem, Product, User
from ..schemas import OrderIn, OrderOut

router = APIRouter(prefix="/api/orders", tags=["orders"])


async def _get_or_create_user(tg: dict, db: AsyncSession) -> User:
    result = await db.execute(select(User).where(User.telegram_id == tg["id"]))
    user = result.scalar_one_or_none()
    if user:
        return user

    user = User(
        telegram_id=tg["id"],
        username=tg.get("username"),
        first_name=tg.get("first_name"),
    )
    db.add(user)
    await db.flush()
    return user


async def _notify_admins(order: Order, customer_name: str) -> None:
    """Send a DM to every admin with the order details."""
    lines = [
        f"🛒 <b>New order #{order.id}</b>",
        "",
        f"👤 <b>{customer_name}</b>",
        f"📞 {order.phone}",
        f"📍 {order.address}",
        "",
        "<b>Items:</b>",
    ]

    for item in order.items:
        lines.append(
            f"  • {item.quantity} × {item.name} — "
            f"Br{int(item.price * item.quantity):,}"
        )

    lines.append("")
    lines.append(f"💰 <b>Total: Br{int(order.total):,}</b>")

    text = "\n".join(lines)

    for admin_id in settings.admin_ids:
        try:
            await bot.send_message(admin_id, text, parse_mode="HTML")
        except Exception as e:
            print(f"[warn] Could not notify admin {admin_id}: {e}")


@router.post("", response_model=OrderOut)
async def create_order(
    payload: OrderIn,
    x_init_data: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    tg_user = get_current_user(x_init_data)

    if not payload.items:
        raise HTTPException(status_code=400, detail="Empty order")

    user = await _get_or_create_user(tg_user, db)
    user.phone = payload.phone or user.phone

    order = Order(
        user_id=user.id,
        total=0.0,
        address=payload.address,
        phone=payload.phone,
        payment_method=payload.payment_method,
        status="pending",
    )
    db.add(order)
    await db.flush()

    total = 0.0
    for item in payload.items:
        result = await db.execute(select(Product).where(Product.id == item.product_id))
        product = result.scalar_one_or_none()
        if not product or not product.is_active:
            raise HTTPException(
                status_code=400, detail=f"Product {item.product_id} unavailable"
            )
        if product.stock < item.quantity:
            raise HTTPException(
                status_code=400, detail=f"Not enough stock for {product.name}"
            )

        product.stock -= item.quantity
        db.add(
            OrderItem(
                order_id=order.id,
                product_id=product.id,
                name=product.name,
                price=product.price,
                quantity=item.quantity,
            )
        )
        total += product.price * item.quantity

    order.total = total
    await db.commit()

    result = await db.execute(
        select(Order).options(selectinload(Order.items)).where(Order.id == order.id)
    )
    full_order = result.scalar_one()

    # Fire off the Telegram DM to admins
    customer_name = tg_user.get("first_name") or tg_user.get("username") or "Customer"
    try:
        await _notify_admins(full_order, customer_name)
    except Exception as e:
        print(f"[warn] Order notification failed: {e}")

    return full_order


@router.get("", response_model=list[OrderOut])
async def my_orders(
    x_init_data: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    tg_user = get_current_user(x_init_data)
    user = await _get_or_create_user(tg_user, db)

    result = await db.execute(
        select(Order)
        .options(selectinload(Order.items))
        .where(Order.user_id == user.id)
        .order_by(Order.created_at.desc())
    )
    return result.scalars().all()


@router.get("/all", response_model=list[OrderOut])
async def all_orders(
    x_init_data: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    tg_user = get_current_user(x_init_data)
    if not is_admin(tg_user["id"]):
        raise HTTPException(status_code=403, detail="Admin only")

    result = await db.execute(
        select(Order)
        .options(selectinload(Order.items))
        .order_by(Order.created_at.desc())
    )
    return result.scalars().all()


@router.put("/{order_id}/status")
async def set_status(
    order_id: int,
    status: str,
    x_init_data: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    tg_user = get_current_user(x_init_data)
    if not is_admin(tg_user["id"]):
        raise HTTPException(status_code=403, detail="Admin only")

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = status
    await db.commit()

    # Notify customer when marked delivered (optional)
    try:
        if status == "delivered" and order.user_id:
            user_q = await db.execute(select(User).where(User.id == order.user_id))
            u = user_q.scalar_one_or_none()
            if u:
                await bot.send_message(
                    u.telegram_id,
                    f"✅ Your order #{order.id} has been marked as <b>delivered</b>. "
                    f"Thank you for shopping with GEBEYA TECH!",
                    parse_mode="HTML",
                )
    except Exception as e:
        print(f"[warn] Could not notify customer: {e}")

    return {"ok": True, "status": order.status}
=======
from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..auth import get_current_user, is_admin
from ..bot import bot
from ..config import settings
from ..database import get_db
from ..models import Order, OrderItem, Product, User
from ..schemas import OrderIn, OrderOut

router = APIRouter(prefix="/api/orders", tags=["orders"])


async def _get_or_create_user(tg: dict, db: AsyncSession) -> User:
    result = await db.execute(select(User).where(User.telegram_id == tg["id"]))
    user = result.scalar_one_or_none()
    if user:
        return user

    user = User(
        telegram_id=tg["id"],
        username=tg.get("username"),
        first_name=tg.get("first_name"),
    )
    db.add(user)
    await db.flush()
    return user


async def _notify_admins(order: Order, customer_name: str) -> None:
    """Send a DM to every admin with the order details."""
    lines = [
        f"🛒 <b>New order #{order.id}</b>",
        "",
        f"👤 <b>{customer_name}</b>",
        f"📞 {order.phone}",
        f"📍 {order.address}",
        "",
        "<b>Items:</b>",
    ]

    for item in order.items:
        lines.append(
            f"  • {item.quantity} × {item.name} — "
            f"Br{int(item.price * item.quantity):,}"
        )

    lines.append("")
    lines.append(f"💰 <b>Total: Br{int(order.total):,}</b>")

    text = "\n".join(lines)

    for admin_id in settings.admin_ids:
        try:
            await bot.send_message(admin_id, text, parse_mode="HTML")
        except Exception as e:
            print(f"[warn] Could not notify admin {admin_id}: {e}")


@router.post("", response_model=OrderOut)
async def create_order(
    payload: OrderIn,
    x_init_data: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    tg_user = get_current_user(x_init_data)

    if not payload.items:
        raise HTTPException(status_code=400, detail="Empty order")

    user = await _get_or_create_user(tg_user, db)
    user.phone = payload.phone or user.phone

    order = Order(
        user_id=user.id,
        total=0.0,
        address=payload.address,
        phone=payload.phone,
        payment_method=payload.payment_method,
        status="pending",
    )
    db.add(order)
    await db.flush()

    total = 0.0
    for item in payload.items:
        result = await db.execute(select(Product).where(Product.id == item.product_id))
        product = result.scalar_one_or_none()
        if not product or not product.is_active:
            raise HTTPException(
                status_code=400, detail=f"Product {item.product_id} unavailable"
            )
        if product.stock < item.quantity:
            raise HTTPException(
                status_code=400, detail=f"Not enough stock for {product.name}"
            )

        product.stock -= item.quantity
        db.add(
            OrderItem(
                order_id=order.id,
                product_id=product.id,
                name=product.name,
                price=product.price,
                quantity=item.quantity,
            )
        )
        total += product.price * item.quantity

    order.total = total
    await db.commit()

    result = await db.execute(
        select(Order).options(selectinload(Order.items)).where(Order.id == order.id)
    )
    full_order = result.scalar_one()

    # Fire off the Telegram DM to admins
    customer_name = tg_user.get("first_name") or tg_user.get("username") or "Customer"
    try:
        await _notify_admins(full_order, customer_name)
    except Exception as e:
        print(f"[warn] Order notification failed: {e}")

    return full_order


@router.get("", response_model=list[OrderOut])
async def my_orders(
    x_init_data: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    tg_user = get_current_user(x_init_data)
    user = await _get_or_create_user(tg_user, db)

    result = await db.execute(
        select(Order)
        .options(selectinload(Order.items))
        .where(Order.user_id == user.id)
        .order_by(Order.created_at.desc())
    )
    return result.scalars().all()


@router.get("/all", response_model=list[OrderOut])
async def all_orders(
    x_init_data: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    tg_user = get_current_user(x_init_data)
    if not is_admin(tg_user["id"]):
        raise HTTPException(status_code=403, detail="Admin only")

    result = await db.execute(
        select(Order)
        .options(selectinload(Order.items))
        .order_by(Order.created_at.desc())
    )
    return result.scalars().all()


@router.put("/{order_id}/status")
async def set_status(
    order_id: int,
    status: str,
    x_init_data: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    tg_user = get_current_user(x_init_data)
    if not is_admin(tg_user["id"]):
        raise HTTPException(status_code=403, detail="Admin only")

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = status
    await db.commit()

    # Notify customer when marked delivered (optional)
    try:
        if status == "delivered" and order.user_id:
            user_q = await db.execute(select(User).where(User.id == order.user_id))
            u = user_q.scalar_one_or_none()
            if u:
                await bot.send_message(
                    u.telegram_id,
                    f"✅ Your order #{order.id} has been marked as <b>delivered</b>. "
                    f"Thank you for shopping with GEBEYA TECH!",
                    parse_mode="HTML",
                )
    except Exception as e:
        print(f"[warn] Could not notify customer: {e}")

    return {"ok": True, "status": order.status}
>>>>>>> 8cd8cd6ae22d7b25daeee3d119f1400c35df92cb
