from fastapi import APIRouter

router= APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_user():
    return {"message": "Lista de ususarios"}
