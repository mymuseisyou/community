"""
URL configuration for community project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), #main>urls.py에서 관리
    path('users/', include('users.urls')), #users>urls.py에서 관리
    path("ckeditor5/", include("django_ckeditor_5.urls")), #ckeditor
    path('tensorflow/', include('tenserfloww.urls')), #tenserfloww>urls.py에서 관리
]
