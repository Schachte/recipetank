from django.test import TestCase

from models import Post


class PostTests(TestCase):

	def test_str(self):
		my_title = Post(name='Title for Test Case')
		self.assertEquals(str(my_title), 'Title for Test Case',

		)
