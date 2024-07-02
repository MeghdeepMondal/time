"""
URL configuration for timeproject project.

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
from django.urls import path

from timenow.views import current_datetime
from time4hrs.views import current_datetime, four_hours_ahead, four_hours_before

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timenow/', current_datetime),
    path('4hrsa/', four_hours_ahead),
    path('4hrsb/', four_hours_before),
]
