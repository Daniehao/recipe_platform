from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UsersViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser', first_name='Mike', last_name='Walows', email='testuser@gmail.com')
        user.set_password('12345')
        user.save()

    def test_login(self):
        # send login data
        login_result = self.client.login(username='testuser', password='12345')
        # should be logged in now
        self.assertTrue(login_result)

    def test_logout(self):
        response = self.client.get(reverse('users:log_out'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_register_valid_form(self):
        response = self.client.post(reverse('users:register'), {
            'username': 'testuser2',
            'first_name': 'Alex',
            'last_name': 'Smith',
            'email': 'testuser2@gmail.com',
            'password1': '1X<ISRUkw+tuK',
            'password2': '1X<ISRUkw+tuK'
        })
        self.assertTrue(User.objects.filter(username='testuser2').exists())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_register_invalid_form(self):
        # Give a password that is too common and does not satisfy the registration criterion
        response = self.client.post(reverse('users:register'), {
            'username': 'testuser3',
            'first_name': 'Alex',
            'last_name': 'Smith',
            'email': 'testuser2@gmail.com',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertFalse(User.objects.filter(username='testuser3').exists())
        self.assertEqual(response.status_code, 200)

    def test_render_register_form(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
