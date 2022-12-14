"""chuck_norris URL Configuration

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
"""
from django.contrib import admin
from django.urls import path

from facts import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('new_fact/', views.new_fact, name='New'),
    path('login/', views.login, name='Login'),
    path('logout/', views.logout, name='Logout'),
    path('admin/', admin.site.urls),
    path('api/facts', views.facts_list),
    path('api/facts/<int:id>', views.fact_detail),
]
