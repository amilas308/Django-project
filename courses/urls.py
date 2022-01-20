from django.urls import path

from .views import our_courses, cs_courses, it_courses

urlpatterns = [
    path('courses/fcsit/all/', our_courses),
    path('courses/fcsit/cs/all/', cs_courses),
    path('courses/fcsit/it/all/', it_courses),
]
