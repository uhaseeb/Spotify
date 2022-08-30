from django import forms
from users.models import User


class SearchForm(forms.Form):
    search = forms.CharField(max_length=70,
                             error_messages={
                                 'required': 'This field is required',
                                 'max_length': 'Max length character exceeds'
                             })


