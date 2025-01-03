# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('edit-dentistry', views.edit_dentistry, name='edit-dentistry'),   
    path('auth-login-basic', views.login, name='auth-login-basic'),   
    path('tao_lich_hen', views.tao_lich_hen, name='tao_lich_hen'),
]

 