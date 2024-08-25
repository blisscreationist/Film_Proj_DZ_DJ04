from django import forms
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review', 'image']  # Добавлено поле image
        labels = {
            'title': 'Название фильма',
            'description': 'Описание фильма',
            'review': 'Отзыв о фильме',
            'image': 'Изображение фильма',
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'}),
            'review': Textarea(attrs={'class': 'form-control'}),
            'image': ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
