from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
 path('login/', views.loginCheck, name='loginCheck'),    
 path('', views.home, name='home'),
 path('company', views.company),  
 path('show',views.show),
 path('show2',views.show),  
 path('edit/<int:id>', views.edit),  
 path('update/<int:id>', views.update),  
 path('delete/<int:id>', views.destroy),
 path('dupload', views.simple_upload),
 path('search', views.search, name="search"),
 path('demo', views.demo, name="demo"),
 path('main',views.main, name="main"),
 path('filter',views.filter, name="filter"),
 path("loginn/", views.login_user, name='login'),
 path("logout/", views.logout_user, name='logout'),
 path("register/", views.register_user, name='register'),
 path('thank_you/', views.thank_you, name='thank_you'),
 path('',include('django.contrib.auth.urls')),
 path('Download',views.download_excel_data, name='download_excel_data'),
 ]

