"""Resumemaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from resume import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.resume,name="resume"),
    path('fresher', views.resume1,name="resume1"),
    path('exp', views.resume2,name="resume2"),
    path('temp', views.resume3,name="resume3"),
    path('about', views.resume4,name="resume4"),
    path('signup', views.resume5,name="resume5"),
    path('data', views.showfromdata,name="showfromdata"),

]

