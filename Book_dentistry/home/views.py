# home/views.py
from django.shortcuts import render

# from django.http import HttpResponse
# from django.template import loader
def home(request):
    return render(request, 'home/main.html')


def account_settings(request):
    return render(request, 'pages-account-settings-account.html')