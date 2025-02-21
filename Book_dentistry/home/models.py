from django.db import models

# Create your models here.
# models.py

class Dentistry:
    def __init__(self, name, address, contact_number, services):
        """
        Khởi tạo đối tượng Dentistry.
        
        Args:
            name (str): Tên phòng khám nha khoa.
            address (str): Địa chỉ phòng khám nha khoa.
            contact_number (str): Số điện thoại liên hệ.
            services (list): Danh sách các dịch vụ mà phòng khám cung cấp.
        """
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.services = services

    def display_info(self):
        """Hiển thị thông tin của phòng khám nha khoa."""
        print(f"Dentistry: {self.name}")
        print(f"Address: {self.address}")
        print(f"Contact: {self.contact_number}")
        print(f"Services: {', '.join(self.services)}")

    def add_service(self, service):
        """Thêm một dịch vụ mới vào danh sách dịch vụ."""
        if service not in self.services:
            self.services.append(service)
            print(f"Service '{service}' has been added.")
        else:
            print(f"Service '{service}' already exists.")

    def remove_service(self, service):
        """Xóa một dịch vụ khỏi danh sách."""
        if service in self.services:
            self.services.remove(service)
            print(f"Service '{service}' has been removed.")
        else:
            print(f"Service '{service}' does not exist.")
    
 
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"
    
    # models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Trường để lưu họ và tên
    phone = models.CharField(max_length=15, blank=True, null=True)  # Trường để lưu số điện thoại
    email = models.EmailField(blank=True, null=True)  # Trường để lưu email (có thể để trống)

    def __str__(self):
        return self.name  # Trả về tên người dùng khi gọi đối tượng UserProfile

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(default='', blank=True)  # Cung cấp giá trị mặc định là chuỗi rỗng
    website = models.URLField(default='', blank=True)  # Cung cấp giá trị mặc định là chuỗi rỗng

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

class CuochenCT(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    is_recurring = models.BooleanField(default=False)
    recurrence_frequency = models.CharField(max_length=50, blank=True, null=True)  # e.g., "monthly"
    duration_months = models.IntegerField(blank=True, null=True)  # e.g., 12 for 12 months

    def send_reminder(self):
        reminder_date = self.appointment_date - timedelta(days=1)
        # Logic to send reminder notification to customer
        return reminder_date

    def __str__(self):
        return f"CuochenCT for {self.customer.user.username} on {self.appointment_date}"

class TreatmentPlan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dentist = models.ForeignKey('Dentist', on_delete=models.CASCADE)
    treatment_description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"Treatment Plan for {self.customer.user.username}"

class Dentist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.user.username} to {self.recipient.user.username} at {self.timestamp}"