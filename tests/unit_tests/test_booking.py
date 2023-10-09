import pytest
from server import app

@pytest.fixture
def client():
    return app.test_client()

def test_purchasePlaces_valid_booking(client):
    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '5'})
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data

def test_purchasePlaces_invalid_booking_more_than_12_places(client):
    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '15'})
    assert response.status_code == 200

def test_purchasePlaces_insufficient_places(client):
    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '50'})
    assert response.status_code == 200

