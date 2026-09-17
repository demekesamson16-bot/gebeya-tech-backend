from datetime import datetime
from pydantic import BaseModel


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    old_price: float | None = None
    image_url: str
    image_urls: list[str] = []
    specs: dict = {}
    warranty: str | None = None
    stock: int
    rating: float
    category_id: int | None = None

    class Config:
        from_attributes = True


class CategoryOut(BaseModel):
    id: int
    name: str
    slug: str

    class Config:
        from_attributes = True


class CartItemIn(BaseModel):
    product_id: int
    quantity: int = 1


class OrderItemOut(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int

    class Config:
        from_attributes = True


class OrderIn(BaseModel):
    items: list[CartItemIn]
    address: str
    phone: str
    payment_method: str = "contact_seller"


class OrderOut(BaseModel):
    id: int
    total: float
    status: str
    payment_method: str
    address: str
    phone: str
    created_at: datetime
    items: list[OrderItemOut]

    class Config:
        from_attributes = True


class ProductIn(BaseModel):
    name: str
    description: str = ""
    price: float
    old_price: float | None = None
    image_url: str = ""
    image_urls: list[str] = []
    specs: dict = {}
    warranty: str | None = None
    stock: int = 0
    category_id: int | None = None


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    old_price: float | None = None
    image_url: str | None = None
    image_urls: list[str] | None = None
    specs: dict | None = None
    warranty: str | None = None
    stock: int | None = None
    category_id: int | None = None
    is_active: bool | None = None


class PhoneSpecOut(BaseModel):
    id: int
    brand: str
    model: str
    release_year: int
    screen_size: str | None = None
    screen_type: str | None = None
    refresh_rate: str | None = None
    battery: str | None = None
    camera_main: str | None = None
    camera_front: str | None = None
    ram: str | None = None
    chipset: str | None = None
    os: str | None = None
    weight: str | None = None
    image_url: str | None = None

    class Config:
        from_attributes = True