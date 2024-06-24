from django.db import models
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from user.models import CustomUser





class Designer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=35)
    fathername = models.CharField(max_length=35)
    phone_number = models.CharField(max_length=40)

    email = models.CharField(max_length=100)
    password = models.CharField(max_length=60)

    name_brang = models.CharField(max_length=50)
    about_designer = models.TextField()
    about_brand = models.TextField()
    for_whom = models.TextField()
    photo_logo=  models.ImageField(upload_to='photos_logo/', null=True)
    styles =  models.TextField(max_length=2000)
    nishes = models.TextField(max_length=2000)

    social_network_1 = models.CharField(max_length=1000)
    social_network_2 = models.CharField(max_length=1000, blank=True, default="не указано")
    social_network_3 = models.CharField(max_length=1000, blank=True, default="не указано")

    investor = models.TextField(max_length=5000)
    money_for_brand = models.TextField(max_length=3000)
    realization = models.TextField(max_length=5000)
    
    comment_suppliers = models.TextField(max_length=5000, blank=True, default="")
    
    document_plan = models.FileField(upload_to='documents/', null=True)


    
    class Meta:
        verbose_name_plural = 'Designers'

class Subscription(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    subscriber = GenericForeignKey('content_type', 'object_id')
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE, related_name='subscriptions_designer')
    time = models.DateTimeField(default=timezone.now)

    @classmethod
    def subscriptions_count(cls, designer):
        return cls.objects.filter(designer=designer).count()

    @classmethod
    def subscribers_count(cls, designer):
        return cls.objects.filter(object_id=designer.pk, content_type=ContentType.objects.get_for_model(Designer)).count()

    @classmethod
    def subscribers_count_user(cls, user):
        return cls.objects.filter(object_id=user.pk, content_type=ContentType.objects.get_for_model(CustomUser)).count()

    


