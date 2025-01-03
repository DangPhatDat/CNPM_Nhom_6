# home/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    return render(request, 'home/home.html')

def account_settings(request):
    return render(request, 'pages-account-settings-account.html')


def edit_dentistry(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/edit-dentistry.html')
    context = {

    }
    return HttpResponse (template.render(context, request))


def login(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/auth-login-basic.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def customer(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/customer.html')
    context = {

    }
    return HttpResponse (template.render(context, request))


def tao_lich_hen(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/tao_lich_hen.html')
    context = {

    }
    return HttpResponse (template.render(context, request))
