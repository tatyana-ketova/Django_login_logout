"""LoginLogout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
    path('special/', special, name='special')
"""

from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static

import basic_app
from LoginLogout import settings
from basic_app import views
from basic_app.views import index, special

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('basic_app/', include('basic_app.urls')),
    path('special/', special, name='special'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
