from rest_framework import generics

from .serializers import CartSerializer
from core.models import Cart


class CartView(generics.ListAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        cart = Cart.objects.filter(user=self.request.user)
        return cart
