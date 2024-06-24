from django.urls import path
from . import views

app_name = 'designer'

urlpatterns = [
    path('registration/', views.registration1, name='registration1'),
    path('step-2/', views.registration2, name='registration2'),
    path('step-3/', views.registration3, name='registration3' ),
    path('step-4/', views.registration4, name='registration4' ),
    path('designer/', views.main_page_designer, name='main_page_designer'),
    path('designer/help/', views.help_page_des, name="help_page_des"), 
    path('logout/', views.logout, name="logout"), 
    path('designer/edit/', views.designer_edit, name="designer_edit"), 
    path('designer/designers/', views.all_designers, name="all_designers"),
    path('designer/investors', views.all_investors, name="all_investors"),
    path('designer-pr/designer/<int:designer_pk>/', views.profile, name='profile'), 
    path('designer/inv-<int:investor_pk>/', views.generate_profile_investor, name='generate_profile_investor'), 
    path('delete_offer/<int:offer_id>/', views.delete_offer, name='delete_offer'),
    path('accept_offer/<int:offer_id>/', views.accept_offer, name='accept_offer'), 
    path('designer/contact-<int:investor_id>/', views.contact_investor, name='contact_investor'), 
    path('designer/subscribe/<int:designer_pk>/', views.subscribe, name='subscribe'),
    path('designer/post/like-<int:post_pk>/', views.like_post_des, name='like_post_des'), 
    
    path('designer/profile-<int:designer_pk>/like-<int:post_pk>/', views.like_post_profile, name='like_post_profile')

]

