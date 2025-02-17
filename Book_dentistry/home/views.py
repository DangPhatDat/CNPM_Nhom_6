# home/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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

def datlaimatkhau(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/datlaimatkhau.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def trongrangimplant(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/trongrangimplant.html')
    context = {

    }
    return HttpResponse (template.render(context, request))


def nhakhoatongquat(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/nhakhoatongquat.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

   

def nhakhoathammy(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/nhakhoathammy.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def niengrang(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/niengrang.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def nhakhoatreem(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/nhakhoatreem.html')
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

def dkphongkham(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/dangkiphongkham.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def benhnhan(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/quanli-lichkham-benhnhan.html')
    context = {

    }
    return HttpResponse (template.render(context, request))


def quanlibacsi(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/quanli-bacsi.html')
    context = {

    }
    return HttpResponse (template.render(context, request))


def chuphongkham(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/chuphongkham.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment  # Tạo model Appointment trước

def submit_appointment(request):
    if request.method == 'POST':
        try:
            # Lấy dữ liệu từ form
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            date = request.POST.get('date')
            time = request.POST.get('time')
            service = request.POST.get('service')

            # Lưu vào database
            Appointment.objects.create(
                name=name,
                phone=phone,
                date=date,
                time=time,
                service=service
            )

            messages.success(request, 'Đặt lịch thành công!')
            return redirect('datlich')  # Chuyển hướng về trang đặt lịch
        except Exception as e:
            messages.error(request, f'Lỗi: {str(e)}')
            return redirect('datlich')
    else:
        return redirect('datlich')


def dangnhapchuphongkham(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/dangnhapchuphongkham.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

