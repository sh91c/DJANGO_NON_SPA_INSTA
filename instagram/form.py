from django import forms

from .models import Post, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo', 'caption', 'location']
        # ModelForm의 widget을 통해 특정 필드에 대한 위젯을 변경할 수 있다.
        widgets = {
            'caption': forms.Textarea,
        }
