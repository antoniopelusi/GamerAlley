from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import (
    my_profile_view,
    ProfileListView,
    accept_invitation,
    reject_invitation,
    send_invitation,
    remove_from_friends,
)


class TestUrls(SimpleTestCase):

    def test_profile_url_is_resolved1(self):
        url = reverse('profiles:my-profile-view')
        self.assertEquals(resolve(url).func, my_profile_view)

    def test_profile_url_is_resolved2(self):
        url = reverse('profiles:all-profiles-view')
        self.assertEquals(resolve(url).func.view_class, ProfileListView)

    def test_profile_url_is_resolved3(self):
        url = reverse('profiles:accept-invite')
        self.assertEquals(resolve(url).func, accept_invitation)

    def test_profile_url_is_resolved4(self):
        url = reverse('profiles:reject-invite')
        self.assertEquals(resolve(url).func, reject_invitation)

    def test_profile_url_is_resolved5(self):
        url = reverse('profiles:send-invite')
        self.assertEquals(resolve(url).func, send_invitation)

    def test_profile_url_is_resolved6(self):
        url = reverse('profiles:remove-friend')
        self.assertEquals(resolve(url).func, remove_from_friends)
