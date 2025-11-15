from fastapi.testclient import TestClient
from main import app  # Import your main FastAPI app instance

client = TestClient(app)


def test():

    # arrange
    item_data = {
        "uuid": "aca49925-9ac5-4109-8125-5ff9caa37552",
        "message": "This is a valid message"
    }

    # act
    response = client.post("/items", json=item_data)

    print(f"response {response}")

    # assert
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["message"] == "Item created successfully"
    assert response_json["is_success"] is True
    assert response_json["data"]["uuid"] == item_data["uuid"]
    assert response_json["data"]["message"] == item_data["message"]
