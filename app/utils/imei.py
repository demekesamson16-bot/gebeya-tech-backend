"""IMEI validation + TAC lookup against the local TAC database."""
import csv
from functools import lru_cache
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent.parent / "data"
_TAC_FILE = _DATA_DIR / "tac_database.csv"


def luhn_check(number: str) -> bool:
    """Luhn checksum validation."""
    if not number.isdigit():
        return False
    total = 0
    for i, ch in enumerate(number[::-1]):
        n = int(ch)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0


def is_valid_imei(imei: str) -> tuple[bool, str]:
    imei = (imei or "").strip().replace(" ", "").replace("-", "")
    if not imei:
        return False, "empty"
    if not imei.isdigit():
        return False, "not_numeric"
    if len(imei) == 16:
        imei = imei[:15]
    if len(imei) != 15:
        return False, f"wrong_length_{len(imei)}"
    if not luhn_check(imei):
        return False, "checksum_failed"
    return True, "ok"


@lru_cache(maxsize=1)
def _load_tac_db() -> dict:
    """Load TAC database.

    Format observed (MoazEb/tac-database):
        Brand, TAC(8 digits), "Specs" (quoted, may contain commas)
    No header row.
    """
    db = {}
    if not _TAC_FILE.exists():
        print(f"[warn] TAC database not found at {_TAC_FILE}")
        return db

    try:
        with open(_TAC_FILE, "r", encoding="utf-8", errors="ignore", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 3:
                    continue

                brand = row[0].strip()
                tac = row[1].strip()
                specs = row[2].strip()

                if tac.lower() == "tac":  # just in case a header sneaks in
                    continue
                if len(tac) != 8 or not tac.isdigit():
                    continue

                if tac not in db and (brand or specs):
                    db[tac] = {
                        "brand": brand or "Unknown",
                        "model": specs or "Unknown device",
                    }
    except Exception as e:
        print(f"[warn] Failed to load TAC database: {e}")

    print(f"[info] Loaded {len(db)} TAC entries")
    return db


def lookup_tac(imei: str) -> dict | None:
    imei = (imei or "").strip().replace(" ", "").replace("-", "")
    if len(imei) < 8 or not imei[:8].isdigit():
        return None
    return _load_tac_db().get(imei[:8])


def analyze_imei(imei: str) -> dict:
    valid, reason = is_valid_imei(imei)
    clean = (imei or "").strip().replace(" ", "").replace("-", "")

    result = {
        "imei": clean,
        "valid": valid,
        "reason": reason,
        "tac": clean[:8] if len(clean) >= 8 else None,
        "serial": clean[8:14] if len(clean) >= 14 else None,
        "check_digit": clean[14] if len(clean) == 15 else None,
        "device": None,
    }

    if valid:
        found = lookup_tac(clean)
        if found:
            result["device"] = found

    return result