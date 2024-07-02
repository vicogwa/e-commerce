from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
     path('', views.cart_detail, name='cart_detail'),  # View the cart
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),  # Add item to cart
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),  # Remove item from cart
    path('update/<int:product_id>/', views.cart_update, name='cart_update'),  
    path('clear/', views.cart_clear, name='cart_clear'),  # Clear the cart
]



