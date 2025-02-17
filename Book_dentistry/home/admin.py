from django.contrib import admin

# Register your models here.
from .models import Clinic

class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'license')
    search_fields = ('name', 'address')

admin.site.register(Clinic, ClinicAdmin)


from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'service')