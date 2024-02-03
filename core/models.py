from django.db import models

# Create your models here.


class user_data(models.Model):
    name=models.CharField(max_length=100,null=True, blank=True)
    email=models.EmailField(max_length=100,null=True, blank=True)
    phone=models.CharField(max_length=20,null=True, blank=True)
    subject=models.CharField(max_length=400,null=True, blank=True)
    message=models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name_plural = 'Customer details'