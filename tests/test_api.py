from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_user() -> None:
    response = client.get("/users/10")

    assert response.status_code == 200

    assert response.json() == {
        "id": 10,
        "name": "Abhi",
        "role": "Backend Developer",
    }
    