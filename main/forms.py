from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['postname', 'username', 'contents']
        labels = {
            'postname': '제목',
            'username': '이름',
            'contents': ' ',
        }