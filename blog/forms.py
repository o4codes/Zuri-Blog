from django.forms import ModelForm
from .models import Post, Comment


class BlogCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('author',None)
        super(BlogCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['title','body']

    def save(self, commit=True):
        instance = super(BlogCreateForm,self).save(commit= False)
        instance.author = self.user

        if commit:
            instance.save()
        return instance
    
class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class CommentListForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body'] 