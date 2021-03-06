"""Ecom URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from App import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', views.index),
    url('signup/', views.signup),
    url('insert/', views.insert),
    url('loginPage/', views.loginPage),
    url('login/', views.login),
    url('cat/', views.cat),
    url('prod/', views.prod),
    url('ProdDetails/', views.ProdDetails),
    url('AddProd/', views.AddProd),
    url('Mycart/', views.Mycart),
    url('Delete/', views.Delete),
    url('logout/', views.logout),

]
