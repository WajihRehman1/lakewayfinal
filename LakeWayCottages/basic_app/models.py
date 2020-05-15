from django.db import models

# Create your models here.
from django.urls import reverse


class features(models.Model):
    image=models.ImageField(upload_to='images',blank=True)
    desc=models.TextField(max_length=250)

    def get_absolute_url(self):
        return reverse("index")


class apartmentType(models.Model):
    ApartmentTitle=models.CharField(max_length=15)
    image=models.ImageField(upload_to='images',blank=True)
    desc=models.TextField(max_length=256)

    def get_absolute_url(self):
        return reverse("index")