from django.test import Client, TestCase


class DashboardHostTests(TestCase):
    def test_home_accepts_runserver_bind_host(self):
        response = Client(HTTP_HOST='0.0.0.0:8000').get('/')

        self.assertEqual(response.status_code, 200)

    def test_home_accepts_localhost(self):
        response = Client(HTTP_HOST='localhost:8000').get('/')

        self.assertEqual(response.status_code, 200)
