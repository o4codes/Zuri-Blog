from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200, default = 'user')
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['created_date']
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)