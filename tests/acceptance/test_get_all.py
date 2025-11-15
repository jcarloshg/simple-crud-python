from fastapi.testclient import TestClient
from main import app  # Import your main FastAPI app instance

client = TestClient(app)


def test():
    # arrange
    # act
    response = client.get("/items")
    # assert
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["message"] == "Items retrieved successfully"
    assert response_json["is_success"] is True
    assert isinstance(response_json["data"], list)
