from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post, Comment


# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email='test@gmail.com',
            password='1234'
        )

        self.post = Post.objects.create(
            title="A good title",
            body="Nice body",
            author=self.user
        )
        
        self.comment = Comment.objects.create(
            body = "Nice post",
            post = self.post,
            name = self.user.username,
        )

    def test_string_representation(self):
        post = Post(title="A simple title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Nice body')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_comment_string_reps(self):
        comment = Comment(body="Nice post")
        self.assertEqual(str(comment), "Comment "+comment.body+" by "+comment.name)

    def test_comment_post(self):
        self.assertEqual(f'{self.post.title}', f'{self.comment.post.title}')
        self.assertEqual(f'{self.user.username}', f'{self.comment.name}') #checks if logged in user made the comment

    def test_post_comment_list(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice post')