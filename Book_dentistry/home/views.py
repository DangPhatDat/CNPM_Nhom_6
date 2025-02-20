# home/views.py

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

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



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # Kiểm tra mật khẩu
        if password != confirm_password:
            messages.error(request, "Mật khẩu không khớp.")
            return redirect('register')

        # Kiểm tra xem email đã tồn tại chưa
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email đã được sử dụng.")
            return redirect('register')

        # Tạo người dùng mới
        user = User.objects.create_user(username=email, password=password, email=email)
        user.save()

        # Tạo hồ sơ người dùng
        user_profile = UserProfile(user=user, name=name, phone=phone, email=email)
        user_profile.save()

        messages.success(request, "Đăng ký thành công!")
        return redirect('dangnhap')  # Chuyển hướng đến trang đăng nhập hoặc trang khác

    return render(request, 'dangky.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    next_url = request.GET.get('next', '/')  # Mặc định chuyển hướng đến trang chính

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_url)  # Chuyển hướng đến URL đã chỉ định
        else:
            # Nếu thông tin đăng nhập không hợp lệ
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng. Vui lòng thử lại.")

    else:
        form = AuthenticationForm()

    return render(request, 'home/dangnhap.html', {'form': form, 'next': next_url})