import pytest
from server import app, competitions, clubs, booked_places

@pytest.fixture
def client():
    return app.test_client()

def test_purchasePlaces_integration(client):
    # Setup: Add a sample competition and club to the test data
    competitions.append({'name': 'Test Competition', 'numberOfPlaces': 10, 'date': '2023-09-20'})
    clubs.append({'name': 'Test Club', 'email': 'test@example.com', 'points': 20})

    # Perform a booking
    response = client.post('/purchasePlaces', data={'competition': 'Test Competition', 'club': 'Test Club', 'places': '5'})
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data

    # Check if the competition's available places and club's points were updated
    competition = next(c for c in competitions if c['name'] == 'Test Competition')
    club = next(c for c in clubs if c['name'] == 'Test Club')
    assert competition['numberOfPlaces'] == 5
    assert club['points'] == 15

    # Check if booked places were updated
    assert booked_places.get('Test Competition') == 5

    # Teardown: Remove the sample competition and club from the test data
    competitions.remove(competition)
    clubs.remove(club)

