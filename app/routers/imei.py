<<<<<<< HEAD
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..utils.imei import analyze_imei

router = APIRouter(prefix="/api/imei", tags=["imei"])


class ImeiRequest(BaseModel):
    imei: str


@router.post("/check")
async def check_imei(payload: ImeiRequest):
    """Public IMEI check. No login required."""
    if not payload.imei or len(payload.imei.strip()) < 3:
        raise HTTPException(status_code=400, detail="Empty IMEI")
=======
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..utils.imei import analyze_imei

router = APIRouter(prefix="/api/imei", tags=["imei"])


class ImeiRequest(BaseModel):
    imei: str


@router.post("/check")
async def check_imei(payload: ImeiRequest):
    """Public IMEI check. No login required."""
    if not payload.imei or len(payload.imei.strip()) < 3:
        raise HTTPException(status_code=400, detail="Empty IMEI")
>>>>>>> 8cd8cd6ae22d7b25daeee3d119f1400c35df92cb
    return analyze_imei(payload.imei)