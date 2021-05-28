from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@email.com', 'testpassword')
        self.post_url = reverse('posts:user-post-view')

    def test_project_post_GET(self):
        self.client.login(username='test', password='testpassword')

        response = self.client.get(self.post_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/myposts.html')

    def test_project_detail_POST_add_new_post(self):
        response = self.client.post(self.post_url, {
            'content': 'content',
            'image': 'image',
            'upvoted': 'upvoted',
            'updated': 'updated',
            'created': 'created',
            'author': 'author',
            'tags': 'tags',
        })

        self.assertEquals(response.status_code, 302)
