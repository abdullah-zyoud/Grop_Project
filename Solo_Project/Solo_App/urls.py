
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('regLog', views.regLog),
    path('book', views.book),
    path('register', views.register),
    path('login', views.login),
    path('admin', views.admin),
    path('user', views.user),
    path('add', views.add), 
    path('addCar', views.addCar),
    path('logout', views.logout),
    path('edit/<int:car_id>', views.edit), 
    path('editCar/<int:car_id>', views.editCar),
    path('delete/<int:car_id>', views.delete),
 
]