# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pages-account-settings-account/', views.account_settings, name='account_settings'),
]

