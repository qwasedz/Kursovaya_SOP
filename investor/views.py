from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import logout as django_logout
from .models import Investor, Offer
from designer.models import Designer, Subscription
from post.models import Like, Post
import os
from django.conf import settings
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
            investor = Investor(
                name = name,
                surname = surname,
                fathername = fathername,
                phone_number = phone_number,
                email = email,
                password = password
            )
            
            investor.save()
            pk = investor.pk
            request.session['user_pk'] = pk
            
            return redirect("http://127.0.0.1:8000/investor/step-2/")
        else:
            return render(request, "registration1_investor.html", {'error_message': 'Заполните все поля)'})
    else:
        return render(request, "registration1_investor.html", {})
    

def registration2(request):
    pk = request.session.get('user_pk')
    if request.method == 'POST':
        cooperation = request.POST.get('cooperation')
        investment = request.POST.get('investment')
        about_investor = request.POST.get('about_investor')
        photo_investor = request.FILES.get('photo_investor')
        
        
        if cooperation and investment and about_investor:
            
            
            # Пытаемся найти объект Designer для этого пользователя
            investor = Investor.objects.get(pk=pk)
            investor.cooperation = cooperation
            investor.investment = investment
            investor.about_investor = about_investor
            if photo_investor:
                investor.photo_investor = photo_investor
                investor.save()
            else:
                investor.save()
            
            
            
            
            return redirect("http://127.0.0.1:8000/investor/step-3/")
        else:
            return render(request, "registration2_investor.html", {'error_message': 'Заполните все поля)'})
    else:
        return render(request, "registration2_investor.html", {})
    
def registration3(request):
    pk = request.session.get('user_pk')
    if request.method == 'POST':
        social_network_1 = request.POST.get('social_network_1')
        social_network_2 = request.POST.get('social_network_2')
        social_network_3 = request.POST.get('social_network_3')
        
        if social_network_1:
           
            investor = Investor.objects.get(pk=pk)
           
            investor.social_network_1 = social_network_1
            investor.social_network_2 = social_network_2
            investor.social_network_3 = social_network_3
            investor.save()
            
            return redirect("http://127.0.0.1:8000/investor/") 
        
        else:
            return render(request, 'registration3_investor.html',{'error_message': 'Не все поля заполнены.'})
    else:
        
        return render(request, 'registration3_investor.html', {})
    
def main_page_investor(request):
    pk = request.session.get('user_pk')
    investor = Investor.objects.get(pk=pk)
    
    offers = Offer.objects.filter(investor=pk)
    return render(request, 'main_page_investor.html', {'investor':investor, 'offers':offers})

def logout_in(request):
    django_logout(request) 
    return redirect("http://127.0.0.1:8000/")

def investor_edit(request):
    pk = request.session.get('user_pk')
    investor = Investor.objects.get(pk=pk)

    if request.method == 'POST':
        if 'edit-base' in request.POST:
            updated_data = {
                'name': request.POST.get('name', investor.name),
                'surname': request.POST.get('surname', investor.surname),
                'fathername': request.POST.get('fathername', investor.fathername),
                'email': request.POST.get('email', investor.email),
                'phone_number': request.POST.get('phone_number', investor.phone_number),
                'password': request.POST.get('password', investor.password),
            }
            
            # Обновляем только те поля профиля дизайнера, которые изменились
            for key, value in updated_data.items():
                setattr(investor, key, value)
        if 'edit-more' in request.POST:
            new_photo = request.FILES.get('photo_investor')
            
            if new_photo:
                # Удаляем старое фото, если оно существует
                if investor.photo_investor:
                    os.remove(os.path.join(settings.MEDIA_ROOT, investor.photo_investor.path))
                
                # Устанавливаем новое фото
                investor.photo_investor = new_photo
            updated_data = {
                'about_investor': request.POST.get('about_investor', investor.about_investor),
                'investment': request.POST.get('investment', investor.investment),
                'cooperation': request.POST.get('cooperation', investor.cooperation)
            }    

            for key, value in updated_data.items():
                setattr(investor, key, value)
        if 'edit-social' in request.POST: 
            updated_data = {
                'social_network_1': request.POST.get('social_network_1', investor.social_network_1),
                'social_network_2': request.POST.get('social_network_2', investor.social_network_2),
                'social_network_3': request.POST.get('social_network_3', investor.social_network_3)
            }   
            for key, value in updated_data.items():
                setattr(investor, key, value)

        investor.save()
        return redirect('investor:investor_edit')
    return render(request, 'investor_edit.html', {'investor':investor})

def help_page_inv(request):
    pk = request.session.get('user_pk')
    investor = Investor.objects.get(pk=pk)

    return render(request, 'investor_help.html', {'investor':investor})

def all_designers_in(request):
    pk = request.session.get('user_pk')
    designers = Designer.objects.all()
    designers_with_subscribers = []
    
    for designer in designers:
        subscribers_count = Subscription.subscriptions_count(designer)
        post_likes = Like.total_likes_count(designer)
        designers_with_subscribers.append({'designer': designer, 'subscribers_count': subscribers_count, 'post_likes':post_likes})
    
    return render(request, 'designers_in.html', {'designers_with_subscribers': designers_with_subscribers, 'pk_inv':pk})


def all_investors_in(request):
    investors = Investor.objects.all()
    return render(request, 'investors_in.html', {'investors':investors})

def profile_des_for_inv(request, designer_pk, pk_inv):
    designer= Designer.objects.get(pk=designer_pk)
    posts = Post.objects.filter(designer=designer_pk)
    podpischiki = Subscription.subscriptions_count(designer)
    podpiski = Subscription.subscribers_count(designer)
    for post in posts:
        post.likes_count = Like.likes_count_for_post(post)
    total_likes = Like.total_likes_count(designer) 
    return render(request, 'des_page_for_inv.html', {'designer':designer, 'posts':posts, 'pk_inv':pk_inv, 'podpischiki': podpischiki,'podpiski':podpiski, 'total_likes':total_likes})




def like_post_profile_inv(request,designer_pk, post_pk):
    
    if request.method == 'POST':
        user_pk = request.session.get('user_pk')
        post = get_object_or_404(Post, pk=post_pk)
        like_type = ContentType.objects.get_for_model(Investor)

        like = Like.objects.filter(post=post, type_user=like_type, who_like=user_pk).exists()
        if not like:
            like = Like.objects.create(post=post, type_user=like_type, who_like=user_pk)
    return redirect('investor:profile_des_for_inv', designer_pk=designer_pk, pk_inv=user_pk)


def profile_inv_for_inv(request, investor_pk):
    investor = Investor.objects.get(pk=investor_pk)
    return render(request, 'investor_page_for_inv.html', {'investor':investor} )


def open_offer(request, designer_pk, pk_inv):
    print(str(pk_inv))
    context = {'designer_pk': designer_pk, 'pk_inv':pk_inv}
    return render(request, 'offer.html', context)

def send_offer(request, designer_pk, pk_inv):
    print(str(pk_inv))
    context = {'designer_pk': designer_pk, 'pk_inv':pk_inv}
    if request.method == 'POST':
        text_offer = request.POST.get('text_offer')
        designer = Designer.objects.get(pk=designer_pk)
        investor=Investor.objects.get(pk=pk_inv)
        
        offer = Offer(
            text_offer = text_offer,
            designer = designer,
            investor = investor
        )
        offer.save()
        return redirect('investor:all_designers_in')
    return render(request, 'offer.html', context)

def delete_offer_in(request, offer_id):
    offer = Offer.objects.get(pk=offer_id)
    offer.status = '2'
    offer.save()
    return redirect('investor:main_page_investor')

def contact_designer(request, designer_id):
    designer = Designer.objects.get(pk=designer_id)
    return render(request, 'connect_des.html', {'designer':designer} )