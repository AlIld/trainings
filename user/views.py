from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from user.models import New_user
from user.forms import RegistrationForm


def showMain(request):
    return render(request, 'user_page/main.html')

def showUser(request, user_id=1):
    return render(request, 'user_page/user.html', context={'users': New_user.objects.all()})

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email = email, password = raw_password)
            login(request, account)
            return redirect('user')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'user_page/register.html', context)