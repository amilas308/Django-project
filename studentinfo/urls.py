from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faculty-of-computing/', include('faculties.urls')),
    path('contacts/', include('contacts.urls')),
    path('a/', include('courses.urls')),
    path('', include('exams.urls'))
]
    
    
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root = settings.STATIC_ROOT
       )
    
    
    
    
    
    
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    
    