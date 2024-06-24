from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Like
from designer.models import Designer
from user.models import CustomUser
from investor.models import Investor
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType

# Create your views here.

def create_new_post(request):
    user_pk = request.session.get('user_pk')
    if request.method == "POST":
        name_post = request.POST.get('name_post')
        description = request.POST.get('description')
        photo_material_url = request.FILES.get('photo_material_url')
        video_material_url = request.FILES.get('video_material_url')
        print(str(photo_material_url))
        print(str(video_material_url))
        if name_post and description:
            designer = get_object_or_404(Designer, pk=user_pk)
            post = Post(
                name_post=name_post,
                description=description,
                designer=designer,
            )
            if photo_material_url and not video_material_url:
                post.photo_material_url = photo_material_url
            elif video_material_url and not photo_material_url:
                post.video_material_url = video_material_url
            elif photo_material_url and video_material_url:
                return HttpResponse('Можно загрузить только один файл: фото или видео')
            else:
                return HttpResponse('Выберите фото или видео для загрузки')
            
            post.save()
            return redirect("designer:main_page_designer")

    return render(request, "new_post.html", {})

