from django.urls import path

from .views import (
    create_faculty,
    update_faculty,
    all_faculties,
    faculty_details,
    #delete_view,
    index
    )

urlpatterns = [
    path('', index, name="home"),
    path('faculties/all/', all_faculties, name="all-faculties"),
    path('create/faculty/', create_faculty),
    path('faculty/<int:id>/details/', faculty_details),
    path('faculty/<int:id>/update/', update_faculty),
    #path('faculty/<int:id>/delete/', update_faculty)
]


