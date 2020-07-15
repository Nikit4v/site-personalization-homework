from django import forms as df
from django.core.exceptions import ValidationError

from auths.models import User


class SignUpForm(df.Form):
    login = df.CharField(label="Login", min_length=4, max_length=150),
    email = df.EmailField(label="Email"),
    password = df.CharField(label="Password", widget=df.PasswordInput)
    confirm = df.CharField(label="Confirm", widget=df.PasswordInput, min_length=8, max_length=32)

    def clean_username(self):
        login = self.cleaned_data['login'].lower()
        r = User.objects.filter(login=login)
        if r.count():
            raise ValidationError("Username already exists")
        return login

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_confirm(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise ValidationError("Password don't match")

        return confirm
