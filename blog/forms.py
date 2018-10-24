from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, null=True, blank=False)
    first_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, required=True, label="password", widget=forms.PasswordInput)
    last_name = forms.CharField(max_length=20)
    date_joined = forms.DateTimeField(auto_now_add=True, auto_now=False)
    date_ = forms.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        model = User