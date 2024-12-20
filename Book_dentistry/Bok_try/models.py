from django.db import models

# Create your models here.
# anh xạ  các couser , student from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    new_field = models.IntegerField(default=0)  # Thêm trường mới
