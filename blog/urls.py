from django.urls import path, include
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, SignUpView,add_comment_to_post
urlpatterns = [
    path('account/',include('django.contrib.auth.urls')),
    path('account/signup/',SignUpView.as_view(), name='signup'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('', BlogListView.as_view(), name='home'),
]
