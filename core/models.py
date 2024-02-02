from django.db import models

# Create your models here.


class user_data(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField(max_length=20)
    subject=models.CharField(max_length=400)
    message=models.TextField()
