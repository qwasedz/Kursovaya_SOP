from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as django_logout
import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .models import Designer, Subscription
from django.utils import timezone
from investor.models import Investor, Offer
from post.models import Like, Post
from django.contrib.contenttypes.models import ContentType

# Create your views here.

def registration1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        fathername = request.POST.get('fathername')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if name and surname and fathername and phone_number and email and password:
            
            
            # Пытаемся найти объект Designer для этого пользователя
            designer = Designer(
                name = name,
                surname = surname,
                fathername = fathername,
                phone_number = phone_number,
                email = email,
                password = password
            )
            
            designer.save()
            pk = designer.pk
            request.session['user_pk'] = pk
            
            return redirect("http://127.0.0.1:8000/step-2/")
        else:
            return render(request, "registration1.html", {'error_message': 'Заполните все поля)'})
    else:
        return render(request, "registration1.html", {})


def registration2(request):
    pk = request.session.get('user_pk')
    if request.method == 'POST' :
        name_brang = request.POST.get('name_brang')
        photo_logo = request.FILES.get('photo_logo')  # Получаем файлы через request.FILES
        about_designer = request.POST.get('about_designer')
        about_brand = request.POST.get('about_brand')
        for_whom = request.POST.get('for_whom')
        styles = request.POST.get('styles')
        nishes = request.POST.get('nishes')
        
        if name_brang and photo_logo and about_designer and about_brand and for_whom and styles and nishes:
            
            
            designer = Designer.objects.get(pk=pk)
            
            designer.name_brang = name_brang
            designer.photo_logo = photo_logo
            designer.about_designer = about_designer
            designer.about_brand = about_brand
            designer.for_whom = for_whom
            designer.styles = styles
            designer.nishes = nishes
            designer.save()
            
            return redirect("http://127.0.0.1:8000/step-3/") 
        
        else:
            return render(request, 'registration2.html',{'error_message': 'Не все поля заполнены.'})
    else:
        
        return render(request, 'registration2.html', {})


def registration3(request):
    pk = request.session.get('user_pk')
    if request.method == 'POST':
        social_network_1 = request.POST.get('social_network_1')
        social_network_2 = request.POST.get('social_network_2')
        social_network_3 = request.POST.get('social_network_3')
        
        if social_network_1:
           
            designer = Designer.objects.get(pk=pk)
           
            designer.social_network_1 = social_network_1
            designer.social_network_2 = social_network_2
            designer.social_network_3 = social_network_3
            designer.save()
            
            return redirect("http://127.0.0.1:8000/step-4/") 
        
        else:
            return render(request, 'registration3.html',{'error_message': 'Не все поля заполнены.'})
    else:
        
        return render(request, 'registration3.html', {})
    
def registration4(request):
    pk = request.session.get('user_pk')
    if request.method == 'POST':
        investor = request.POST.get('investor')
        money_for_brand = request.POST.get('money_for_brand')
        realization = request.POST.get('realization')
        comment_suppliers = request.POST.get('comment_suppliers')
        document_plan = request.FILES.get('document_plan')
        if investor and money_for_brand and realization and comment_suppliers:
            
            designer = Designer.objects.get(pk=pk)
            
            designer.investor = investor
            designer.money_for_brand = money_for_brand
            designer.realization = realization
            designer.comment_suppliers = comment_suppliers
            
            if document_plan:
                designer.document_plan = document_plan
                designer.save()
            else:
                designer.save()
            
            return redirect("http://127.0.0.1:8000/designer/") 
        
        else:
            return render(request, 'registration4.html',{'error_message': 'Не все поля заполнены.'})
    else:
        
        return render(request, 'registration4.html', {})
    

def designer_edit(request):
    pk = request.session.get('user_pk')
    designer = Designer.objects.get(pk=pk)

    if request.method == 'POST':
        if 'edit-brand' in request.POST:
            # Получаем новое фото из запроса
            new_photo = request.FILES.get('photo_logo')
            
            if new_photo:
                # Удаляем старое фото, если оно существует
                if designer.photo_logo:
                    os.remove(os.path.join(settings.MEDIA_ROOT, designer.photo_logo.path))
                
                # Устанавливаем новое фото
                designer.photo_logo = new_photo
            
            updated_data = {
                'name_brang': request.POST.get('name_brang', designer.name_brang),
                'about_designer': request.POST.get('about_designer', designer.about_designer),
                'about_brand': request.POST.get('about_brand', designer.about_brand),
                'for_whom': request.POST.get('for_whom', designer.for_whom),
                'styles': request.POST.get('styles', designer.styles),
                'nishes': request.POST.get('nishes', designer.nishes),
            }
            
            # Обновляем только те поля профиля дизайнера, которые изменились
            for key, value in updated_data.items():
                setattr(designer, key, value)

        if 'edit-base' in request.POST:
            updated_data = {
                'name': request.POST.get('name', designer.name),
                'surname': request.POST.get('surname', designer.surname),
                'fathername': request.POST.get('fathername', designer.fathername),
                'email': request.POST.get('email', designer.email),
                'phone_number': request.POST.get('phone_number', designer.phone_number),
                'password': request.POST.get('password', designer.password),
            }
            
            # Обновляем только те поля профиля дизайнера, которые изменились
            for key, value in updated_data.items():
                setattr(designer, key, value)

        if 'edit-investor' in request.POST:
            new_doc = request.FILES.get('document_plan')
            
            if new_doc:
                # Удаляем старое фото, если оно существует
                if designer.document_plan:
                    os.remove(os.path.join(settings.MEDIA_ROOT, designer.document_plan.path))
                
                # Устанавливаем новое фото
                designer.document_plan = new_doc
            updated_data = {
                'investor': request.POST.get('investor', designer.investor),
                'money_for_brand': request.POST.get('money_for_brand', designer.money_for_brand),
                'realization': request.POST.get('realization', designer.realization),
                'comment_suppliers': request.POST.get('comment_suppliers', designer.comment_suppliers)
            }
            for key, value in updated_data.items():
                setattr(designer, key, value)

        designer.save()
        return redirect('designer:designer_edit')

    return render(request, "designer_edit.html", {'designer': designer})


    
def main_page_designer(request):

    pk = request.session.get('user_pk')
    designer = Designer.objects.get(pk=pk)
    offers = Offer.objects.filter(designer=pk)
    posts = Post.objects.filter(designer=pk)
    
    podpischiki = Subscription.subscriptions_count(designer)
    podpiski = Subscription.subscribers_count(designer)

    for post in posts:
        post.likes_count = Like.likes_count_for_post(post)
    total_likes = Like.total_likes_count(designer)  
    return render(request, 'main_designer.html', {'designer': designer, 'posts':posts, 'offers':offers,  'podpischiki': podpischiki,'podpiski':podpiski, 'total_likes':total_likes})

def help_page_des(request):
    return render(request, "des_help.html", {}) 

def logout(request):
    django_logout(request)
    return redirect("http://127.0.0.1:8000/")


def all_designers(request):
    designers = Designer.objects.all()
    designers_with_subscribers = []
    
    for designer in designers:
        subscribers_count = Subscription.subscriptions_count(designer)
        post_likes = Like.total_likes_count(designer)
        designers_with_subscribers.append({'designer': designer, 'subscribers_count': subscribers_count, 'post_likes': post_likes})
        

    return render(request, 'designers.html', {'designers_with_subscribers': designers_with_subscribers})
def all_investors(request):
    investors = Investor.objects.all()
    return render(request, 'investors.html', {'investors':investors})




def profile(request, designer_pk):
    designer= Designer.objects.get(pk=designer_pk)
    posts = Post.objects.filter(designer=designer_pk)
    podpischiki = Subscription.subscriptions_count(designer)
    podpiski = Subscription.subscribers_count(designer)
   
    for post in posts:
        post.likes_count = Like.likes_count_for_post(post)
    total_likes = Like.total_likes_count(designer)   
    return render(request, 'des_page_for_des_user.html', {'designer':designer, 'posts':posts, 'podpischiki': podpischiki,'podpiski':podpiski , 'total_likes':total_likes})


def subscribe(request, designer_pk):
    user_pk = request.session.get('user_pk')
    if request.method == 'POST':
        designer_podpisals = get_object_or_404(Designer, pk=user_pk)
        designer_na_kogo = get_object_or_404(Designer, pk=designer_pk)
        
        # Проверка, существует ли уже подписка
        subscription_exists = Subscription.objects.filter(
            content_type=ContentType.objects.get_for_model(designer_podpisals),
            object_id=user_pk,
            designer=designer_na_kogo
        ).exists()

        if not subscription_exists:
            subscription = Subscription.objects.create(
                content_type=ContentType.objects.get_for_model(designer_podpisals),
                object_id=user_pk,
                designer=designer_na_kogo
            )
        
    return redirect('designer:profile', designer_pk=designer_pk)


def like_post_des(request, post_pk):
    
    if request.method == 'POST':
        user_pk = request.session.get('user_pk')
        post = get_object_or_404(Post, pk=post_pk)
        like_type = ContentType.objects.get_for_model(Designer)

        like = Like.objects.filter(post=post, type_user=like_type, who_like=user_pk).exists()
        if not like:
            like = Like.objects.create(post=post, type_user=like_type, who_like=user_pk)
    return redirect('designer:main_page_designer')
    
def like_post_profile(request,designer_pk, post_pk):
    
    if request.method == 'POST':
        user_pk = request.session.get('user_pk')
        post = get_object_or_404(Post, pk=post_pk)
        like_type = ContentType.objects.get_for_model(Designer)

        like = Like.objects.filter(post=post, type_user=like_type, who_like=user_pk).exists()
        if not like:
            like = Like.objects.create(post=post, type_user=like_type, who_like=user_pk)
    return redirect('designer:profile', designer_pk=designer_pk)
    

def generate_profile_investor(request, investor_pk):
    investor = Investor.objects.get(pk=investor_pk)
    return render(request, 'investor_page_for_des.html', {'investor':investor} )

def delete_offer(request, offer_id):
    offer = Offer.objects.get(pk=offer_id)
    offer.status = '2'
    offer.save()
    return redirect('designer:main_page_designer')

def accept_offer(request, offer_id):
    offer = Offer.objects.get(pk=offer_id)
    offer.status = '1'  # Изменяем статус на 'Доступно'
    offer.save()        # Сохраняем изменения
    return redirect('designer:main_page_designer')

def contact_investor(request, investor_id):
    investor = Investor.objects.get(pk=investor_id)
    return render(request, 'connect.html', {'investor':investor} )


