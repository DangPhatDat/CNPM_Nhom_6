# home/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('trangchu', views.trangchu, name='trangchu'),
    path('gioithieu', views.gioithieu, name='gioithieu'),
    path('dichvu', views.dichvu, name='dichvu'),
    path('banggia', views.banggia, name='banggia'),
    path('uudai', views.uudai, name='uudai'),
    path('datlich', views.datlich, name='datlich'),
    path('dangnhap', views.dangnhap, name='dangnhap'),
    path('quenmatkhau', views.quenmatkhau, name='quenmatkhau'),
    path('dangky', views.dangky, name='dangky'),
     path('datlaimatkhau', views.datlaimatkhau, name='datlaimatkhau'),
    
 

]

 