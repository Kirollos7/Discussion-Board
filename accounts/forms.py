from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=255,required=True)
    last_name = forms.CharField(max_length=255,required=True)
    email = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1', 'password2')
