from django.shortcuts import render

from user.models import New_user

def home_screen_view(request):
    context = {}

    accounts = New_user.objects.all()
    context['accounts'] = accounts

    return render(request, 'personal/home.html', context)
