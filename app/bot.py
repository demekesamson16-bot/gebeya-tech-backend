from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonWebApp,
    Message,
    WebAppInfo,
)

from .config import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛍 Open GEBEYA TECH",
                    web_app=WebAppInfo(url=settings.WEBAPP_URL),
                )
            ],
            [
                InlineKeyboardButton(
                    text="📦 My Orders",
                    url=f"{settings.WEBAPP_URL}/orders",
                )
            ],
            [
                InlineKeyboardButton(
                    text="💬 Contact Support",
                    url="https://t.me/GebeyaEnhid_bot",
                )
            ],
        ]
    )


@dp.message(CommandStart())
async def cmd_start(message: Message):
    name = message.from_user.first_name or "friend"
    text = (
        f"👋 <b>Welcome to GEBEYA TECH</b>, {name}!\n\n"
        "Your one-stop shop for <b>phones, laptops & tech gear</b> "
        "right inside Telegram.\n\n"
        "Tap the button below to browse the catalog 👇"
    )
    await message.answer(text, reply_markup=main_menu_kb(), parse_mode="HTML")


@dp.message(Command("shop"))
async def cmd_shop(message: Message):
    await message.answer(
        "Tap to open the store 👇",
        reply_markup=main_menu_kb(),
    )


@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Available commands:\n"
        "/start – Main menu\n"
        "/shop – Open the store\n"
        "/help – Show this help\n\n"
        "Need help? Message @GebeyaEnhid_bot",
    )


@dp.message(F.text)
async def fallback(message: Message):
    await message.answer(
        "Tap the button below to browse the store 👇",
        reply_markup=main_menu_kb(),
    )


async def setup_menu_button():
    """Set the persistent menu button that opens the Mini App."""
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="🛍 Shop",
            web_app=WebAppInfo(url=settings.WEBAPP_URL),
        )
    )
    