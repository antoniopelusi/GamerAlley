from django.contrib.auth.models import User
from django.test import TestCase
from ..models import Profile


class TestModels(TestCase):

    def test_create_user(self):
        user = User.objects.create_user('test', 'test@email.com', 'testpassword')

        self.assertEquals(str(user), 'test')
        self.assertEquals(str(user.email), 'test@email.com')

    def test_create_profile(self):
        profile = Profile(
            'field1',
            'field2',
            'field3',
            'field4',
            'field5',
            'field5',
            'field6',
            'field6',
            'field8',
            'field9',
            'field10',
        )

        self.assertEquals(str(profile.first_name), 'field2')
        self.assertEquals(str(profile.last_name), 'field3')
