"""User service functions."""


def get_user(user_id: int) -> dict[str, object]:
    """Return user information for the given user ID."""
    return {
        "id": user_id,
        "name": "Abhi",
        "role": "Backend Developer",
    }
