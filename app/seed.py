from sqlalchemy import select

from .database import SessionLocal
from .models import Category, Product


SEED_DATA = [
    ("Phones", "phones", [
        {
            "name": "iPhone 13 · 128GB · Used",
            "description": "A15 Bionic chip · Super Retina XDR display · 98% battery health · 1-year GEBEYA TECH warranty.",
            "price": 70000,
            "old_price": 75000,
            "image_url": "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=800",
            "stock": 3,
        },
        {
            "name": "Samsung Galaxy A54 · 5G · New",
            "description": "6.4\" Super AMOLED · 5000 mAh · sealed box · 1-year warranty.",
            "price": 38500,
            "old_price": None,
            "image_url": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=800",
            "stock": 10,
        },
        {
            "name": "Tecno Camon 20 Pro",
            "description": "64MP camera · 8GB RAM · 256GB storage · 5000 mAh battery.",
            "price": 24500,
            "old_price": 27000,
            "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800",
            "stock": 12,
        },
    ]),
    ("Laptops", "laptops", [
        {
            "name": "MacBook Air M2 · 256GB",
            "description": "Apple M2 chip · 8GB RAM · 13.6\" Liquid Retina · macOS Sonoma.",
            "price": 128000,
            "old_price": 135000,
            "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800",
            "stock": 4,
        },
        {
            "name": "HP EliteBook 840 G8",
            "description": "Intel i5 11th gen · 16GB RAM · 512GB SSD · 14\" FHD.",
            "price": 62000,
            "old_price": None,
            "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800",
            "stock": 6,
        },
    ]),
    ("Accessories", "accessories", [
        {
            "name": "AirPods Pro 2 · USB-C",
            "description": "Active noise cancellation · spatial audio · sealed.",
            "price": 12000,
            "old_price": 13500,
            "image_url": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=800",
            "stock": 25,
        },
        {
            "name": "Anker 20K Power Bank",
            "description": "20000 mAh · 65W PD fast charge · dual USB-C.",
            "price": 4500,
            "old_price": None,
            "image_url": "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=800",
            "stock": 40,
        },
        {
            "name": "Logitech MX Master 3S",
            "description": "Pro wireless mouse · 8K DPI · silent clicks.",
            "price": 8900,
            "old_price": None,
            "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=800",
            "stock": 15,
        },
    ]),
]


async def seed_if_empty():
    """Fill the DB with sample products, only if it's completely empty."""
    async with SessionLocal() as db:
        result = await db.execute(select(Product).limit(1))
        if result.scalar_one_or_none():
            return

        for cat_name, cat_slug, products in SEED_DATA:
            cat = Category(name=cat_name, slug=cat_slug)
            db.add(cat)
            await db.flush()

            for p in products:
                db.add(Product(
                    name=p["name"],
                    description=p["description"],
                    price=p["price"],
                    old_price=p["old_price"],
                    image_url=p["image_url"],
                    stock=p["stock"],
                    rating=4.6,
                    category_id=cat.id,
                ))

        await db.commit()
        