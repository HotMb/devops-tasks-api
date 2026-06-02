import sys
sys.path.insert(0, 'src')
from app import app
def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
def test_add_task():
    client = app.test_client()
    response = client.post('/tasks', json={"title": "Test"})
    assert response.status_code == 200
    assert "id" in response.json

def test_delete_task():
    client = app.test_client()

    # Création
    response = client.post('/tasks', json={"title": "Test"})
    assert response.status_code == 201
    assert "id" in response.json

    task_id = response.json["id"]

    # Suppression
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 200

    # Vérification
    response = client.get('/tasks')
    assert response.status_code == 200
    assert len(response.json) == 0
