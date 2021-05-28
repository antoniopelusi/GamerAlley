from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@email.com', 'testpassword')
        self.profile_url = reverse('profiles:my-profile-view')

    def test_project_profile_GET(self):
        self.client.login(username='test', password='testpassword')

        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/myprofile.html')

    def test_project_detail_POST_add_new_relationship(self):
        response = self.client.post(self.profile_url, {
            'sender': 'me',
            'receiver': 'you',
            'status': 'send',
            'updated': '10',
            'created': '01',
        })

        self.assertEquals(response.status_code, 302)
