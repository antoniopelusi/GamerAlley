from django.test import SimpleTestCase
from ..forms import ProfileModelForm


class TestForms(SimpleTestCase):

    def test_form_valid_data(self):
        form = ProfileModelForm(
            data={
                'first_name': 'firstname',
                'last_name': 'lastname',
                'bio': 'biography',
                'avatar': 'avatar',
            }
        )

        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = ProfileModelForm(
            data={}
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

