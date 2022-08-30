from django import forms
from .models import User


class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Enter Username',
            'email': 'Enter Email',
            'password': 'Enter Password'
            }
        error_messages = {
            'username': {
             'required': 'This field is required',
             'max_length': 'Max length should not exceed'
        }
    }
