from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from user.models import New_user

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required, Add a valid email address')

    class Meta:
        model = New_user
        fields = ("email", "username", "password1", "password2")

class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = New_user
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid login")

class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = New_user
        fields = ("email", "username")

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = New_user.objects.exclude(pk=self.instance.pk).get(email=email)
            except New_user.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = New_user.objects.exclude(pk=self.instance.pk).get(username=username)
            except New_user.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % username)