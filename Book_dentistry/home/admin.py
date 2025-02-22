from django.contrib import admin

# Register your models here.
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'service')

from django.contrib import admin
from .models import Clinic, UserProfile

class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email', 'website')
    search_fields = ('name', 'address')
    list_filter = ('address',)

admin.site.register(Clinic, ClinicAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone', 'role')
    list_filter = ('role',)
    search_fields = ('name', 'email', 'phone')

admin.site.register(UserProfile, UserProfileAdmin)