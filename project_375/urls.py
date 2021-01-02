"""project375_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from project_375.apps.cabinet.views import index, privacy
from .yasg import urlpatterns as doc_urls
from django.contrib import admin






urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/', include('project_375.core.urls')),
    url('^test/', include('project_375.apps.tests.urls')),
    url('^$', index),
    path('', include('social_django.urls')),
    path('privacy/', privacy),
    ]
urlpatterns += doc_urls




