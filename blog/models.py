from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class BlogUser(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(unique=True,max_length=300)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.email
