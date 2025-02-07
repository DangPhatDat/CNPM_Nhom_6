# home/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import datlichForm

def home(request):
    return render(request, 'home/trangchu.html')

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
    
def trangchu(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/trangchu.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def gioithieu(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/gioithieu.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def dichvu(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/dichvu.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def banggia(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/banggia.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def uudai(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/uudai.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def datlich(request):
    if request.method == "POST":
        form = datlichForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/home/trangchu.html")


        pass

    template = loader.get_template('home/datlich.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def dangnhap(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/dangnhap.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def quenmatkhau(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/quenmatkhau.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def dangky(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/dangky.html')
    context = {

    }
    return HttpResponse (template.render(context, request))


def editdangki(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/editdangki.html')
    context = {

    }
    return HttpResponse (template.render(context, request))
