from django.db import models
from designer.models import Designer

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Post(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    name_post = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    photo_material_url = models.ImageField(upload_to='posts/img/', null=True)
    video_material_url = models.FileField(upload_to='posts/video/', null=True)
    date = models.DateField(auto_now=True)

   
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type_user = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    who_like = models.PositiveIntegerField()
    like = GenericForeignKey('type_user', 'who_like')
    
    @classmethod
    def likes_count_for_post(cls, post):
        return cls.objects.filter(post=post).count()

    @classmethod
    def total_likes_count(cls, designer):
        total_likes = 0
        posts = Post.objects.filter(designer=designer)
        for post in posts:
            total_likes += cls.likes_count_for_post(post)
        return total_likes