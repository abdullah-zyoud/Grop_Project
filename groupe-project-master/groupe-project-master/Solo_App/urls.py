
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('regLog', views.regLog),
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
    path('addToCart', views.add_to_cart),
    path('cart', views.cart),	  
    path('checkout', views.checkout), 
    # path('bookmark', views.bookmark),
    path('add_favorite/<int:car_id>', views.add_to_favorites),
    path('remove_favorite/<int:car_id>', views.remove_from_favorites),
    path('bookmark', views.show_favorites),
]