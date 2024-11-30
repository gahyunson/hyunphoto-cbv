from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import (
    PhotoSerializer,
    PhotoDetailSerializer,
)
from core.models import (
    Photos
)


class PhotoView(generics.ListAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [AllowAny]


class PhotoDetailView(generics.ListAPIView):
    serializer_class = PhotoDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Photos.objects.filter(id=self.kwargs['photo_id'])
        return queryset
