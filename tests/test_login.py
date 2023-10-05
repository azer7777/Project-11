from server import app

client = app.test_client()

def test_showSummary_valid_user(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200  # HTTP OK

def test_showSummary_invalid_user(client):
    response = client.post('/showSummary', data={'email': 'unknown@example.com'})
    assert response.status_code == 302  # HTTP Redirect