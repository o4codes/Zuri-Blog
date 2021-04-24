from django import forms
from .models import BlogUser


class BlogUserForm(forms.ModelForm):
    class Meta:
        model = BlogUser
        fields = ['name','email','password']
        widgets = {
            'password': forms.PasswordInput()
        }

class BlogUserLogin(forms.ModelForm):
    class Meta:
        model = BlogUser
        fields = ['email','password']
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailField()
        }