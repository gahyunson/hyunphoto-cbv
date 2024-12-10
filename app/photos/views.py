from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import (
    PhotoSerializer,
    PhotoDetailSerializer,
)
from core.models import (
    Photos
)


class PhotoView(generics.ListCreateAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        if Photos.objects.filter(title=title):
            return Response({'message': 'Already exist'}, status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)


class PhotoDetailView(generics.ListCreateAPIView):
    serializer_class = PhotoDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Photos.objects.filter(id=self.kwargs['photo_id'])
        return queryset
