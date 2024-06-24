from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.start_page, name='start_page' ),
    path('help/', views.help_page, name='help_page'),
    path('auth/', views.entry, name="entry"), 
   

]