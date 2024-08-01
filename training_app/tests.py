from django.test import TestCase , client
from .models import Post ,Blog
from django.urls import reverse
from django.contrib.auth import get_user_model

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
        )
        self.post = Blog.objects.create(
        title='A good title',
        body='Nice body content',
        author=self.user,
        )
    def test_string_representation(self):
        post = Blog(title='A sample title')
        self.assertEqual(str(post), post.title)
    def test_blog_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')
    def test_blog_list_view(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog.html')

    def test_blog_detail_view(self):
        response = self.client.get('/blog/1/')
        no_response = self.client.get('/blog/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'blog_detail.html')

class SimpleTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')
        
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')