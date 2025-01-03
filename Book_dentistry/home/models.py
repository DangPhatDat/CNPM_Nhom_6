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
