from django.test import TestCase
from ..models import Post


class TestModels(TestCase):

    def test_create_post(self):
        post = Post(
            'field1',
            'field2',
            'field3',
            'field4',
            'field5',
            'field6',
            'field7',
        )

        self.assertEquals(str(post.content), 'field2')
        self.assertEquals(str(post.image), 'field3')
