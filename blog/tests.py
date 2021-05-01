"""
    blog/tests.py
    -------------
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view_no_response(self):
        no_response = self.client.get('/post/1000/')
        self.assertEqual(no_response.status_code, 404)

    def test_post_detail_view_response(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_response_template_and_contains(self):
        """
        To test:    1. Assert a response
                    2. Assert a template rendering the response
        """
        r = self.client.get('/post/1/')
        self.assertContains(r, 'A good title')
        self.assertTemplateUsed(r, 'detail.html')

    def test_post_create_view(self):
        """ C: Check if create works. """
        response = self.client.post(reverse('new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self):
        """ U: Check if update works. """
        response = self.client.post(reverse('edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 200)

    def test_post_delete_view(self):
        """ D: Check if delete works. """
        response = self.client.get(reverse('delete', args='1'))
        self.assertEqual(response.status_code, 200)
