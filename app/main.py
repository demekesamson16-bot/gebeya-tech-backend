from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from aiogram.types import Update

from .config import settings
from .database import Base, engine
from .bot import bot, dp, setup_menu_button
from .routers import products, orders, uploads, checklists, imei
from .seed import seed_if_empty


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await seed_if_empty()
    try:
        await setup_menu_button()
    except Exception as e:
        print(f"[warn] Could not set menu button: {e}")
    yield
    await bot.session.close()


app = FastAPI(title="GEBEYA TECH API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(uploads.router)
app.include_router(checklists.router)
app.include_router(imei.router)

UPLOAD_DIR = Path(__file__).resolve().parent.parent / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=str(UPLOAD_DIR)), name="uploads")


@app.get("/health")
async def health():
    return {"status": "ok", "app": "GEBEYA TECH"}


@app.post("/webhook/{secret}")
async def telegram_webhook(secret: str, request: Request):
    expected = settings.BOT_TOKEN.split(":")[0]
    if secret != expected:
        return {"ok": False}
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)
    return {"ok": True}
