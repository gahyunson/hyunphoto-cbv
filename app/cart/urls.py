from django.urls import path

from cart import views


app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
]
