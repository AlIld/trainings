from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import New_user

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required, Add a valid email address')

    class Meta:
        model = New_user
        fields = ("email", "username", "password1", "password2")