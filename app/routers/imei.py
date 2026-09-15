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
    return analyze_imei(payload.imei)