from django.urls import path
from django.urls.conf import re_path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
