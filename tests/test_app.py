import os

os.environ.setdefault("OPENROUTER_API_KEY", "test-key")

from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
    assert set(response.json["agents"]) == {"support", "marketing", "tutor"}


def test_missing_message():
    client = app.test_client()
    response = client.post("/generate", json={"agent": "support"})
    assert response.status_code == 400


def test_invalid_agent():
    client = app.test_client()
    response = client.post("/generate", json={"agent": "unknown", "message": "hello"})
    assert response.status_code == 400
