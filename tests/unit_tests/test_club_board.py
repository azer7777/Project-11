import pytest
from server import app, clubs

@pytest.fixture
def client():
    return app.test_client()

def test_clubs_info_route(client):
    response = client.get('/clubsInfo')
    assert response.status_code == 200
    # Check if the response contains the expected content
    assert b'Clubs Information' in response.data  # text is present in 'clubs_info.html' template
    for club in clubs:
        assert club['name'].encode() in response.data