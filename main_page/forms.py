from django import forms
from .models import *
from django.forms import TextInput


class LinksForm(forms.ModelForm):
    original = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder' : 'Введите ссылку...',
        }
    ))

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Дайте описание...',
        }
    ))

    class Meta:
        model = Links
        fields = (
            'original',
            'description',
            'tag',
        )
        # exclude = [""]


