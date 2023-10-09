import pytest
from server import app

@pytest.fixture
def client():
    return app.test_client()

def test_logout_route(client):
    response = client.get('/logout')
    assert response.status_code == 302