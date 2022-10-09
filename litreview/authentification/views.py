from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings

from . import forms


class LoginPage(View):
    form_class = forms.LoginForm
    template_name = 'authentification/login.html'

    def get(self, request):
        form = self.form_class
        message = ''
        return render(
            request, self.template_name,
            context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('feed')
            else:
                message = 'identifiants invalides.'
        return render(
            request, self.template_name,
            context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(
        request,
        'authentification/signup.html',
        context={'form': form})
