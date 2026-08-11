from fastapi import FastAPI

from app.services import get_user

app = FastAPI(title="Quality Pipeline API")


@app.get("/")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/users/{user_id}")
def read_user(user_id: int) -> dict[str, object]:
    return get_user(user_id)
