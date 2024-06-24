from django.urls import path
from . import views


app_name="post"
urlpatterns = [
    path('designer/new_post/', views.create_new_post, name='create_new_post'),
    
]
