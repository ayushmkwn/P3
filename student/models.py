from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    First_Name = models.CharField(max_length=20)
    Middle_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=7)
    Address = models.CharField(max_length=100)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=10)
    Alternate_Email = models.EmailField()
    Alternate_Mobile = models.CharField(max_length=10)
    Father_Name = models.CharField(max_length=50)
    Mother_Name = models.CharField(max_length=50)
    Institute_Name = models.CharField(max_length=50)
    Branch_Name = models.CharField(max_length=50)
