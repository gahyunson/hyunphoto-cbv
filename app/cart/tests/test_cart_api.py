"""Tests for cart APIs."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Photos, Prices, Cart

from cart.serializers import CartSerializer

import tempfile

CART_URL = reverse('cart:cart')


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


def create_photos(**params):
    """Create and return a photo sample data."""
    sample = {
        'title': 'The night',
        'description': 'The night we used to rock.',
        'image': tempfile.NamedTemporaryFile(suffix=".jpg").name
    }
    sample.update(params)
    photo = Photos.objects.create(**sample)

    return photo


def create_prices(photo, **params):
    """Create and return a price of a photo."""
    price_sample = {
        'photo': photo,
        'size': '20x16"',
        'price': 86.0
    }
    price_sample.update(params)
    price = Prices.objects.create(**price_sample)

    return price


def create_cart(user, photo, price, **params):
    """Create cart to my cart."""
    defaults = {
        'user': user,
        'photo': photo,
        'price': price,
        'quantity': 1
    }
    defaults.update(params)
    cart = Cart.objects.create(**defaults)

    return cart


class PrivateCartApiTests(TestCase):
    """Test cart API authenticated."""
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='gahyun@example.com', password='macbook')
        self.client.force_authenticate(self.user)

    def test_cart_list_success(self):
        """Successfully GET the authenticated user's cart list."""
        photo = create_photos()
        price = create_prices(photo)
        create_cart(self.user, photo, price)
        user2 = create_user(
            **{
                'email': 'user2@example.com',
                'password': 'user2123',
                'name': 'User Two'
            }
        )
        create_cart(user2, photo, price)

        res = self.client.get(CART_URL)

        cart = Cart.objects.filter(user=self.user)
        serializer = CartSerializer(cart, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), len(serializer.data))
