from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re


class LoginForm(forms.Form):

    email_regex = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    email_validator = RegexValidator(
        regex=email_regex,
        message="Digite um endereço de e-mail válido.",
        code='invalid_email'
    )

    email = forms.CharField(
        validators=[email_validator],
        widget=forms.TextInput(attrs={
            # 'class': 'form-control',
            'placeholder': 'Digite seu e-mail'
        }))
    
    password_regex = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"
    password_validator = RegexValidator(
        regex=password_regex,
        message="Digite um senha válido",
        code='invalid_password'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            # 'class': 'form-control',
            'placeholder': 'Digite sua senha'
        }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match(self.email_regex, email):
            raise ValidationError("Digite um endereço de e-mail válido.")
        return email
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if not re.match(self.password_regex, password):
            raise ValidationError("Digite um senha válido")
        return password
