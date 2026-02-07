import sys
from importlib.util import find_spec
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

HAS_FLASK = find_spec("flask") is not None
HAS_PROM = find_spec("prometheus_client") is not None


def test_dependencies_are_declared() -> None:
    requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8")

    assert "Flask==" in requirements
    assert "gunicorn==" in requirements
    assert "prometheus-client==" in requirements


@pytest.mark.skipif(not (HAS_FLASK and HAS_PROM), reason="runtime dependencies not installed")
def test_index_endpoint() -> None:
    from app import create_app

    client = create_app().test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Flask DevOps showcase is running"


@pytest.mark.skipif(not (HAS_FLASK and HAS_PROM), reason="runtime dependencies not installed")
def test_health_endpoint() -> None:
    from app import create_app

    client = create_app().test_client()
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


@pytest.mark.skipif(not (HAS_FLASK and HAS_PROM), reason="runtime dependencies not installed")
def test_readiness_endpoint() -> None:
    from app import create_app

    client = create_app().test_client()
    response = client.get("/readyz")

    assert response.status_code == 200
    assert response.get_json()["ready"] is True
