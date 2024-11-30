from rest_framework import generics, status, authentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import CartSerializer
from core.models import Cart


class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.filter(user=self.request.user)
        return cart

    def patch(self, request, *args, **kwargs):
        cart_id = self.request.data.get('cart_id')
        cart = Cart.objects.get(id=cart_id)
        serializer = CartSerializer(cart, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        cart_id = request.data.get('cart_id')
        cart = Cart.objects.get(id=cart_id)
        cart.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
