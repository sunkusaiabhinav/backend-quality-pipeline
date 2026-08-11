"""Main FastAPI application."""

from fastapi import FastAPI

from app.services import get_user

app = FastAPI(title="Quality Pipeline API")


@app.get("/")
def health_check() -> dict[str, str]:
    """Return the health status of the API."""
    return {"status": "healthy"}


@app.get("/users/{user_id}")
def read_user(user_id: int) -> dict[str, object]:
    """Return user information for the given user ID."""
    return get_user(user_id)
