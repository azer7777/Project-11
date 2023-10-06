import pytest
from server import app

@pytest.fixture
def client():
    return app.test_client()

def test_purchasePlaces_insufficient_points(client):
    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Iron Temple', 'places': '5'})
    assert response.status_code == 200
    assert b'Great-booking complete!' not in response.data

