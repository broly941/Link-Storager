from django import forms
from .models import *

class LinksForm(forms.ModelForm):
    original = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder' : 'Enter the link...',
        }
    ))

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter the  description...',
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


