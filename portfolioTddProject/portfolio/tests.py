from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Image,Portfolio,UserP
import json

# Create your tests here.
class PortfolioTestCase(TestCase):

    def test_list_portfolios_status(self):
        url = '/portfolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_list_portfolios_count(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        user_p = UserP.objects.create(user=user_model,photo='', professional_profile= 'profProf1')
        image = Image.objects.create(name='nuevo', url='No', description='testImage', type='private')
        Portfolio.objects.create(name='nuevo', description='testImage', image=image, user=user_p)
        Portfolio.objects.create(name='nuevo2', description='testImage', image=image,  user=user_p)
        Portfolio.objects.create(name='nuevo3', description='testImage', image=image, user=user_p)

        url = '/portfolio/'
        response = self.client.get(url, format='json')
        current_data = json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data), 3)