from django.test import SimpleTestCase
from ..forms import PostModelForm


class TestForms(SimpleTestCase):

    def test_form_valid_data(self):
        form = PostModelForm(
            data={
                'content': 'text',
                'tags': 'tag',
                'image': 'img',
            }
        )

        self.assertFalse(form.is_valid())

    def test_form_no_data(self):
        form = PostModelForm(
            data={}
        )

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
