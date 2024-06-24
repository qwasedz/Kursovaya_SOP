from django.db import models
from designer.models import Designer

class Investor(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=35)
    fathername = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=60)

    cooperation = models.TextField()
    investment = models.TextField()
    about_investor = models.TextField()
    photo_investor=  models.ImageField(upload_to='photos_investor/', null=True)

    social_network_1 = models.CharField(max_length=1000)
    social_network_2 = models.CharField(max_length=1000, blank=True, default="не указано")
    social_network_3 = models.CharField(max_length=1000, blank=True, default="не указано")


class Offer(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    text_offer = models.TextField(max_length=3000, blank=True, default="")
    status = models.CharField(max_length=20, choices=[('0', 'Ожидание'), ('1', 'Доступно'), ('2', 'Отмена')], default='0')
