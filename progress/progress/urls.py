from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('service.urls')),
    re_path(r'^celery-progress/', include('celery_progress.urls')), 
]
