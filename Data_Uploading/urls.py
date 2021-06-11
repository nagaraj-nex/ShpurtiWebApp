from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
 #path("about/", views.about, name="AboutUs"),
 path('company', views.company),  
 path('show',views.show),  
 path('edit/<int:id>', views.edit),  
 path('update/<int:id>', views.update),  
 path('delete/<int:id>', views.destroy),
 path('dupload', views.simple_upload),
 path('search', views.search, name="search"),
 path('demo', views.demo, name="demo"),
 path('csv',views.getfile, name="getfile"),
 path('main',views.main, name="main"),
 path('filter',views.filter, name="filter"),
 

 ]

