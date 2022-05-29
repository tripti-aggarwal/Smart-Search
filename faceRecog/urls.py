"""faceRecog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path, include
from django.contrib import admin
from faceRecog import views as app_views

urlpatterns = [
    re_path(r'^$', app_views.index),
    re_path(r'^error_image$', app_views.errorImg),
    re_path(r'^create_dataset$', app_views.create_dataset),
    re_path(r'^trainer$', app_views.trainer),
    re_path(r'^eigen_train$', app_views.eigenTrain),
    re_path(r'^detect$', app_views.detect),
    re_path(r'^detect_image$', app_views.detectImage),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^records/', include('records.urls')),
]
