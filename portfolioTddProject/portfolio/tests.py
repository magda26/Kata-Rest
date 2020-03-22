from django.contrib.auth.models import User
from django.test import TestCase, Client


# Create your tests here.
class PortfolioTestCase(TestCase):

    def test_list_portfolios_status(self):
        url = '/portfolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

