import os
from fastapi import Request, HTTPException, status
from jose import jwt, JWTError
from app.tables import SessionLocal

JWT_SECRET = os.getenv("JWT_SECRET", "your_jwt_secret")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def verify_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No token provided."
        )

    try:
        jwt.decode(auth_header, JWT_SECRET, algorithms=["HS256"])
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {str(e)}"
        )