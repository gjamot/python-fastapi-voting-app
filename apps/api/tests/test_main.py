from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_get_post_not_found():
    response = client.get("/api/posts/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Post not found"

# after adding test data you can do:
# def test_get_post_found():
#     response = client.get("/api/posts/1")
#     assert response.status_code == 200
#     assert "id" in response.json()