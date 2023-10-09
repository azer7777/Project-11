from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def index(self):
        self.client.get('/')

    @task
    def login_and_book(self):
        response = self.client.post('/showSummary', data={'email': 'john@simplylift.co'})
        if 'Welcome' in response.text:
            competition_name = 'Spring Festival'
            club_name = 'Simply Lift'
            self.client.get(f'/book/{competition_name}/{club_name}')

    @task
    def view_clubs_info(self):
        self.client.get('/clubsInfo')

    @task
    def logout(self):
        self.client.get('/logout')
