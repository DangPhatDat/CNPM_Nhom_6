# doctors/forms.py
from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'experience']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên Bác Sĩ'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Chuyên Khoa'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Số Năm Kinh Nghiệm'}),
        }
        
from django import forms
from .models import Clinic

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'address', 'phone_number', 'email', 'website']