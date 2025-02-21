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


def trangchubacsi(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/trangchubacsi.html')
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

# doctors/views.py


# View thêm bác sĩ mới
from django.shortcuts import render, redirect
from .models import Doctor

def add_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('doctor-name')
        specialty = request.POST.get('doctor-specialty')
        experience = request.POST.get('doctor-experience')

        # Kiểm tra nếu đã nhập đầy đủ thông tin
        if name and specialty and experience:
            # Tạo đối tượng Doctor và lưu vào database
            doctor = Doctor(name=name, specialty=specialty, experience=int(experience))
            doctor.save()

            # Sau khi lưu, chuyển hướng về trang danh sách bác sĩ
            return redirect('doctor_list')

    # Nếu là GET hoặc nhập thiếu thông tin, hiển thị lại trang thêm bác sĩ
    return render(request, 'add_doctor.html')



def add_doctor(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/add_doctor.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def doctor_list(request):
    if request.method == "POST":
        pass

    template = loader.get_template('home/doctor_list.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def dkphongkham(request):
    if request.method == "POST":
        pass

    template = loader.get_template('chuphongkham/dkphongkham.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

from django.shortcuts import render, redirect
from .forms import ClinicForm
from .models import Clinic

def dkphongkham(request):
    if request.method == 'POST':
        form = ClinicForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu thông tin vào cơ sở dữ liệu
            return redirect('dkphongkham')  # Redirect để tránh gửi lại form
    else:
        form = ClinicForm()

    clinics = Clinic.objects.all()  # Lấy tất cả phòng khám từ database
    return render(request, 'chuphongkham/dkphongkham.html', {'form': form, 'clinics': clinics})

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CuochenCT, Customer

@login_required
def dklichkham(request):
    if request.method == 'POST':
        appointment_date = request.POST.get('appointment_date')
        is_recurring = request.POST.get('is_recurring') == 'True'
        recurrence_frequency = request.POST.get('recurrence_frequency', '')
        duration_months = request.POST.get('duration_months', None)

        # Lưu lịch khám vào cơ sở dữ liệu
        customer = Customer.objects.get(user=request.user)
        cuochen = CuochenCT(
            customer=customer,
            appointment_date=appointment_date,
            is_recurring=is_recurring,
            recurrence_frequency=recurrence_frequency,
            duration_months=duration_months
        )
        cuochen.save()

        # Chuyển hướng đến trang thành công hoặc trang khác
        return redirect('success_page')  # Thay 'success_page' bằng tên URL bạn muốn chuyển hướng đến

    return render(request, 'dklichkham.html')

def dklichkham(request):
    if request.method == "POST":
        pass

    template = loader.get_template('khachhang/dklichkham.html')
    context = {

    }
    return HttpResponse (template.render(context, request))

def success_page(request):
    if request.method == "POST":
        pass

    template = loader.get_template('khachhang/success.html')
    context = {

    }
    return HttpResponse (template.render(context, request))
