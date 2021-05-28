from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import (
    post_comment_create_and_list_view,
    upvote_downvote_post,
    user_post_view,
)


class TestUrls(SimpleTestCase):

    def test_post_url_is_resolved1(self):
        url = reverse('posts:main-post-view')
        self.assertEquals(resolve(url).func, post_comment_create_and_list_view)

    def test_post_url_is_resolved2(self):
        url = reverse('posts:upvote-post-view')
        self.assertEquals(resolve(url).func, upvote_downvote_post)

    def test_post_url_is_resolved3(self):
        url = reverse('posts:user-post-view')
        self.assertEquals(resolve(url).func, user_post_view)
