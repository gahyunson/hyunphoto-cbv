from rest_framework import generics

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


class PhotoDetailView(generics.ListAPIView):
    serializer_class = PhotoDetailSerializer

    def get_queryset(self):
        queryset = Photos.objects.filter(id=self.kwargs['photo_id'])
        return queryset
