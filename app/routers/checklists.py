<<<<<<< HEAD
from fastapi import APIRouter, HTTPException, Query

from ..checklists import (
    CHECKLISTS,
    get_checklist,
    get_checklist_preview,
    get_safety_page,
)

router = APIRouter(prefix="/api/checklists", tags=["checklists"])


@router.get("/safety")
async def safety_page(lang: str = Query("en")):
    """Full Safety page content: promise + all category checklists."""
    if lang not in ("en", "am"):
        lang = "en"
    return get_safety_page(lang)


@router.get("/{category_slug}")
async def checklist_for_category(
    category_slug: str,
    lang: str = Query("en"),
):
    """Checklist for a specific category in the requested language."""
    if category_slug not in CHECKLISTS:
        raise HTTPException(status_code=404, detail="Unknown category")
    if lang not in ("en", "am"):
        lang = "en"

    checklist = get_checklist(category_slug, lang)
    return {
        **checklist,
        "preview": get_checklist_preview(category_slug, lang),
=======
from fastapi import APIRouter, HTTPException, Query

from ..checklists import (
    CHECKLISTS,
    get_checklist,
    get_checklist_preview,
    get_safety_page,
)

router = APIRouter(prefix="/api/checklists", tags=["checklists"])


@router.get("/safety")
async def safety_page(lang: str = Query("en")):
    """Full Safety page content: promise + all category checklists."""
    if lang not in ("en", "am"):
        lang = "en"
    return get_safety_page(lang)


@router.get("/{category_slug}")
async def checklist_for_category(
    category_slug: str,
    lang: str = Query("en"),
):
    """Checklist for a specific category in the requested language."""
    if category_slug not in CHECKLISTS:
        raise HTTPException(status_code=404, detail="Unknown category")
    if lang not in ("en", "am"):
        lang = "en"

    checklist = get_checklist(category_slug, lang)
    return {
        **checklist,
        "preview": get_checklist_preview(category_slug, lang),
>>>>>>> 8cd8cd6ae22d7b25daeee3d119f1400c35df92cb
    }