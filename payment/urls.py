from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.payment_page, name='payment_page'),  # View the payment page
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),  # Create a Stripe checkout session
    path('success/', views.payment_success, name='payment_success'),  # Payment success page
    path('cancel/', views.payment_cancel, name='payment_cancel'),  # Payment cancel page
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),  # Stripe webhook for events
]
