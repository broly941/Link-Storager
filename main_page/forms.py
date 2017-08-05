from django import forms
from .models import *


class LinksForm(forms.ModelForm):

    class Meta:
        model = Links
        exclude = [""]

