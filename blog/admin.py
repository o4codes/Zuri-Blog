from django.contrib import admin
from .models import Post, BlogUser

# Register your models here.
admin.site.register(Post)
admin.site.register(BlogUser)