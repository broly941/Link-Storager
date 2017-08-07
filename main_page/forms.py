from django import forms
from .models import *
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )

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


User = get_user_model()

class UserLoginForm(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder' : 'Логин...',
    #     }
    # ))
    #
    # password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Пароль...',
    #     }
    # ))

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count == 1:
        #     user =user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not longer active')
        return super(UserLoginForm, self).clean(*args, **kwargs)

