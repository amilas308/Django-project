from django.urls import path

from .views import departments


urlpatterns = [
    path('depts', departments)
]
