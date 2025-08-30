from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'tags', 'text', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "заголовок (максимальная длина 200 символов)"
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'Заголовок поста:',
            'category': 'Категория:',
            'tags': 'Теги:',
            'text': 'Текст поста:',
            'image': 'Картинка поста'
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if len(title) < 5:
            raise forms.ValidationError("Заголовок не должен быть короче 5 символов")
        
        return title
