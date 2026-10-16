import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import app as app_module


@pytest.fixture(autouse=True)
def reset_tasks():
    app_module.tasks.clear()
    yield
    app_module.tasks.clear()


def test_health():
    response = app_module.app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_add_task():
    response = app_module.app.test_client().post("/tasks", json={"title": "Test"})
    assert response.status_code == 201
    assert "id" in response.json


def test_delete_task():
    client = app_module.app.test_client()

    response = client.post("/tasks", json={"title": "Test"})
    assert response.status_code == 201
    task_id = response.json["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
    assert response.data == b""

    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json == []
