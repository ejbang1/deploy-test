from fastapi.responses import JSONResponse
from fastapi import APIRouter, FastAPI

router = APIRouter()

@router.get("/test")
def test(): 
    return JSONResponse(
        status_code=200,
        content={"message" : "test"}
    )
