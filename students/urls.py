from django.urls import path
from .views import buk_students, about_us


urlpatterns = [
    path('', buk_students),
    path('about/', about_us), 
]