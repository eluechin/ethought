from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('login/', views.login, name='login'),
    path('add_cart/<int:item_id>/', views.add_cart, name="add_cart"),
    path('cart/<int:cart_id>/', views.cart, name='cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name="remove_from_cart"),
    path('review/<int:item_id>/', views.review, name="review"),
    path('logout/', views.logout, name='logout')
]
