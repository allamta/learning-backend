from pathlib import Path
import sys

from fastapi.testclient import TestClient


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import app


client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze_returns_expected_matches() -> None:
    response = client.post(
        "/api/analyze",
        json={"text": "oats with sugar and salt"},
    )

    assert response.status_code == 200
    body = response.json()

    assert body["assessments"]["Oats"]["rating"] == "healthy"
    assert body["assessments"]["Sugar"]["rating"] == "unhealthy"
    assert body["assessments"]["Salt"]["rating"] == "neutral"


def test_analyze_rejects_empty_text() -> None:
    response = client.post("/api/analyze", json={"text": "   "})

    assert response.status_code == 400
    assert response.json() == {"detail": "text must not be empty"}
