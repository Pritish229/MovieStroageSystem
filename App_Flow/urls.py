from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('movie',views.movie, name ='movie'),
    path('moviesum', views.moviesum, name='moviesum'),
    path('', views.showdata, name='showdata'),
    path('showdata/<int:pk>', views.editdata, name='editpageinfo'),
    path('deletedata/<int:pk>', views.deletedata, name='deleteinfo'),


] 
