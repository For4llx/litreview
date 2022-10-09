from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'}))
    password = forms.CharField(
        max_length=63,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))


class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Mot de passe'}),
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Confirmer mot de passe'}),
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)
        labels = {
          "username": ""
        }
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Nom d\'utilisateur'})
        }
        help_texts = {
            'username': None,
        }
