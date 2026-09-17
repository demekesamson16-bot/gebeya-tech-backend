from sqlalchemy import select

from .database import SessionLocal
from .models import Category, Product, PhoneSpec


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
        
        # ── Phone Specs Seed Data ─────────────────────────────────────
PHONE_SPECS = [
    # ── APPLE ─────────────────────────────────────────────
    {"brand": "Apple", "model": "iPhone 15 Pro Max", "release_year": 2023,
     "screen_size": "6.7\"", "screen_type": "LTPO Super Retina XDR OLED", "refresh_rate": "120 Hz",
     "battery": "4441 mAh", "camera_main": "48 MP", "camera_front": "12 MP",
     "ram": "8 GB", "chipset": "Apple A17 Pro", "os": "iOS 17", "weight": "221 g"},
    {"brand": "Apple", "model": "iPhone 15", "release_year": 2023,
     "screen_size": "6.1\"", "screen_type": "Super Retina XDR OLED", "refresh_rate": "60 Hz",
     "battery": "3349 mAh", "camera_main": "48 MP", "camera_front": "12 MP",
     "ram": "6 GB", "chipset": "Apple A16 Bionic", "os": "iOS 17", "weight": "171 g"},
    {"brand": "Apple", "model": "iPhone 14", "release_year": 2022,
     "screen_size": "6.1\"", "screen_type": "Super Retina XDR OLED", "refresh_rate": "60 Hz",
     "battery": "3279 mAh", "camera_main": "12 MP", "camera_front": "12 MP",
     "ram": "6 GB", "chipset": "Apple A15 Bionic", "os": "iOS 16", "weight": "172 g"},
    {"brand": "Apple", "model": "iPhone 13", "release_year": 2021,
     "screen_size": "6.1\"", "screen_type": "Super Retina XDR OLED", "refresh_rate": "60 Hz",
     "battery": "3240 mAh", "camera_main": "12 MP", "camera_front": "12 MP",
     "ram": "4 GB", "chipset": "Apple A15 Bionic", "os": "iOS 15", "weight": "174 g"},
    {"brand": "Apple", "model": "iPhone 12", "release_year": 2020,
     "screen_size": "6.1\"", "screen_type": "Super Retina XDR OLED", "refresh_rate": "60 Hz",
     "battery": "2815 mAh", "camera_main": "12 MP", "camera_front": "12 MP",
     "ram": "4 GB", "chipset": "Apple A14 Bionic", "os": "iOS 14", "weight": "164 g"},

    # ── SAMSUNG ───────────────────────────────────────────
    {"brand": "Samsung", "model": "Galaxy S24 Ultra", "release_year": 2024,
     "screen_size": "6.8\"", "screen_type": "LTPO AMOLED", "refresh_rate": "120 Hz",
     "battery": "5000 mAh", "camera_main": "200 MP", "camera_front": "12 MP",
     "ram": "12 GB", "chipset": "Snapdragon 8 Gen 3", "os": "Android 14", "weight": "232 g"},
    {"brand": "Samsung", "model": "Galaxy S24", "release_year": 2024,
     "screen_size": "6.2\"", "screen_type": "Dynamic AMOLED 2X", "refresh_rate": "120 Hz",
     "battery": "4000 mAh", "camera_main": "50 MP", "camera_front": "12 MP",
     "ram": "8 GB", "chipset": "Exynos 2400", "os": "Android 14", "weight": "167 g"},
    {"brand": "Samsung", "model": "Galaxy S23", "release_year": 2023,
     "screen_size": "6.1\"", "screen_type": "Dynamic AMOLED 2X", "refresh_rate": "120 Hz",
     "battery": "3900 mAh", "camera_main": "50 MP", "camera_front": "12 MP",
     "ram": "8 GB", "chipset": "Snapdragon 8 Gen 2", "os": "Android 13", "weight": "168 g"},
    {"brand": "Samsung", "model": "Galaxy S21", "release_year": 2021,
     "screen_size": "6.2\"", "screen_type": "Dynamic AMOLED 2X", "refresh_rate": "120 Hz",
     "battery": "4000 mAh", "camera_main": "12 MP", "camera_front": "10 MP",
     "ram": "8 GB", "chipset": "Exynos 2100", "os": "Android 11", "weight": "169 g"},
    {"brand": "Samsung", "model": "Galaxy S8", "release_year": 2017,
     "screen_size": "5.8\"", "screen_type": "Super AMOLED", "refresh_rate": "60 Hz",
     "battery": "3000 mAh", "camera_main": "12 MP", "camera_front": "8 MP",
     "ram": "4 GB", "chipset": "Exynos 8895", "os": "Android 7", "weight": "155 g"},

    # ── GOOGLE ────────────────────────────────────────────
    {"brand": "Google", "model": "Pixel 8 Pro", "release_year": 2023,
     "screen_size": "6.7\"", "screen_type": "LTPO OLED", "refresh_rate": "120 Hz",
     "battery": "5050 mAh", "camera_main": "50 MP", "camera_front": "10.5 MP",
     "ram": "12 GB", "chipset": "Google Tensor G3", "os": "Android 14", "weight": "213 g"},
    {"brand": "Google", "model": "Pixel 8", "release_year": 2023,
     "screen_size": "6.2\"", "screen_type": "OLED", "refresh_rate": "120 Hz",
     "battery": "4575 mAh", "camera_main": "50 MP", "camera_front": "10.5 MP",
     "ram": "8 GB", "chipset": "Google Tensor G3", "os": "Android 14", "weight": "187 g"},
    {"brand": "Google", "model": "Pixel 7", "release_year": 2022,
     "screen_size": "6.3\"", "screen_type": "AMOLED", "refresh_rate": "90 Hz",
     "battery": "4355 mAh", "camera_main": "50 MP", "camera_front": "10.8 MP",
     "ram": "8 GB", "chipset": "Google Tensor G2", "os": "Android 13", "weight": "197 g"},
    {"brand": "Google", "model": "Pixel 6", "release_year": 2021,
     "screen_size": "6.4\"", "screen_type": "AMOLED", "refresh_rate": "90 Hz",
     "battery": "4614 mAh", "camera_main": "50 MP", "camera_front": "8 MP",
     "ram": "8 GB", "chipset": "Google Tensor", "os": "Android 12", "weight": "207 g"},

    # ── HUAWEI ────────────────────────────────────────────
    {"brand": "Huawei", "model": "Mate 60 Pro", "release_year": 2023,
     "screen_size": "6.82\"", "screen_type": "LTPO OLED", "refresh_rate": "120 Hz",
     "battery": "5000 mAh", "camera_main": "50 MP", "camera_front": "13 MP",
     "ram": "12 GB", "chipset": "Kirin 9000S", "os": "HarmonyOS 4.0", "weight": "225 g"},
    {"brand": "Huawei", "model": "P60 Pro", "release_year": 2023,
     "screen_size": "6.67\"", "screen_type": "LTPO OLED", "refresh_rate": "120 Hz",
     "battery": "4815 mAh", "camera_main": "48 MP", "camera_front": "13 MP",
     "ram": "8 GB", "chipset": "Snapdragon 8+ Gen 1", "os": "HarmonyOS 3.1", "weight": "200 g"},
    {"brand": "Huawei", "model": "P40 Pro", "release_year": 2020,
     "screen_size": "6.58\"", "screen_type": "OLED", "refresh_rate": "90 Hz",
     "battery": "4200 mAh", "camera_main": "50 MP", "camera_front": "32 MP",
     "ram": "8 GB", "chipset": "Kirin 990 5G", "os": "Android 10", "weight": "209 g"},
    {"brand": "Huawei", "model": "P30 Pro", "release_year": 2019,
     "screen_size": "6.47\"", "screen_type": "OLED", "refresh_rate": "60 Hz",
     "battery": "4200 mAh", "camera_main": "40 MP", "camera_front": "32 MP",
     "ram": "8 GB", "chipset": "Kirin 980", "os": "Android 9", "weight": "192 g"},
]


async def seed_phone_specs():
    """Seed the phone_specs table with reference data."""
    async with SessionLocal() as db:
        r = await db.execute(select(PhoneSpec).limit(1))
        if r.scalar_one_or_none():
            return  # already seeded
        for spec in PHONE_SPECS:
            db.add(PhoneSpec(**spec))
        await db.commit()
        print(f"✅ Seeded {len(PHONE_SPECS)} phone specs")