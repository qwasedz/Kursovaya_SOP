from django.urls import path
from . import views

app_name = 'investor'

urlpatterns = [
    path('investor/step-1/', views.registration1, name='registration1'),
    path('investor/step-2/', views.registration2, name='registration2'),
    path('investor/step-3/', views.registration3, name='registration3'),
    path('investor/', views.main_page_investor, name='main_page_investor'),
    path('logout/', views.logout_in, name="inv-logout"), 
    path('investor/edit/', views.investor_edit, name='investor_edit'), 
    path('investor/help/', views.help_page_inv, name='help_page_inv'),
    path('investor/designers/', views.all_designers_in, name='all_designers_in'), 
    path('investor/investors/', views.all_investors_in, name='all_investors_in'),
    path('investor-<int:pk_inv>/des-<int:designer_pk>/', views.profile_des_for_inv, name='profile_des_for_inv'), 
    path('investor/inv-<int:investor_pk>/', views.profile_inv_for_inv, name='profile_inv_for_inv'), 
    path('investor-<int:pk_inv>/open-des<int:designer_pk>/', views.open_offer, name='open_offer'),
    path('investor-<int:pk_inv>/send-des<int:designer_pk>/', views.send_offer, name='send_offer'), 
    path('investor/delete_offer/<int:offer_id>/', views.delete_offer_in, name='delete_offer_in'),
    path('investor/contact-<int:designer_id>/', views.contact_designer, name='contact_designer'), 
    path('investor/profile-<int:designer_pk>/like-<int:post_pk>/', views.like_post_profile_inv, name='like_post_profile_inv')
    
]
