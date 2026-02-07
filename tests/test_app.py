import pytest

pytest.importorskip("flask")
pytest.importorskip("prometheus_client")

from app import create_app


def test_index_endpoint() -> None:
    client = create_app().test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Flask DevOps showcase is running"


def test_health_endpoint() -> None:
    client = create_app().test_client()
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_readiness_endpoint() -> None:
    client = create_app().test_client()
    response = client.get("/readyz")

    assert response.status_code == 200
    assert response.get_json()["ready"] is True
