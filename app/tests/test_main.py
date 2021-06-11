from fastapi.testclient import TestClient
from main import app
from mangum import Mangum

client = TestClient(app)


def test_main_resource():
    response_auth = client.get(f"/")
    assert response_auth.status_code == 200


def test_child_resource():
    response_auth = client.get(f"/api/v1/test")
    assert response_auth.status_code == 200

handler = Mangum(app, spec_version=2)