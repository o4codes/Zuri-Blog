from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Comment
from .forms import BlogCreateForm, CommentCreateForm, CommentListForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    


class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = BlogCreateForm
    queryset = Post.objects.all()

    def get_form_kwargs(self):
        kwargs = super(BlogCreateView,self).get_form_kwargs()
        kwargs.update({'author': self.request.user})
        return kwargs


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = request.user.username
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentCreateForm()
    return render(request, 'comment_new.html', {'form': form})

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




