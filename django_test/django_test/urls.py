"""
URL configuration for django_test project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),        # HTML
    path('api/', include('students.api_urls')), # API REST
]
