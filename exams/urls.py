from django.urls import path

from .views import allExams, cs_exams, it_exams


urlpatterns = [
    path('all/', allExams),
    path('cs/', cs_exams),
    path('it/', it_exams),
]
