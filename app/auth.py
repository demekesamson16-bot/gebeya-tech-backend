import hashlib
import hmac
import json
from urllib.parse import parse_qsl

from fastapi import Header, HTTPException

from .config import settings


def validate_init_data(init_data: str) -> dict:
    """Validate Telegram WebApp initData per the official spec."""
    if not init_data:
        raise HTTPException(status_code=401, detail="Missing initData")

    try:
        parsed = dict(parse_qsl(init_data, strict_parsing=True))
    except ValueError:
        raise HTTPException(status_code=401, detail="Malformed initData")

    received_hash = parsed.pop("hash", None)
    if not received_hash:
        raise HTTPException(status_code=401, detail="Missing hash")

    data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(parsed.items()))
    secret_key = hmac.new(
        b"WebAppData", settings.BOT_TOKEN.encode(), hashlib.sha256
    ).digest()
    computed = hmac.new(
        secret_key, data_check_string.encode(), hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(computed, received_hash):
        raise HTTPException(status_code=401, detail="Invalid initData signature")

    return parsed


def get_current_user(x_init_data: str = Header(default="")) -> dict:
    # ------------------------------------------------------------------
    # DEV MODE BYPASS
    # If no initData is provided (i.e., we're testing in a normal browser,
    # not inside Telegram), treat the first admin in ADMIN_TELEGRAM_IDS
    # as the current user. This lets us test the admin panel locally.
    #
    # ⚠️ Remove this block before making the app public.
    # ------------------------------------------------------------------
    if not x_init_data or x_init_data.strip() == "":
        if settings.admin_ids:
            return {
                "id": settings.admin_ids[0],
                "first_name": "Admin",
                "username": "admin",
            }

    parsed = validate_init_data(x_init_data)
    user_raw = parsed.get("user", "{}")
    try:
        user = json.loads(user_raw)
    except json.JSONDecodeError:
        raise HTTPException(status_code=401, detail="Invalid user data")

    if not user.get("id"):
        raise HTTPException(status_code=401, detail="No user in initData")
    return user


def is_admin(telegram_id: int) -> bool:
    return telegram_id in settings.admin_ids
