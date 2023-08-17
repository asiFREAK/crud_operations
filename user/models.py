from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    confirm_password = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
