from django.urls import path

from photos import views


app_name = 'photos'

urlpatterns = [
    path('', views.PhotoView.as_view(), name='photos-list'),
    path('<int:photo_id>/', views.PhotoDetailView.as_view(),
         name='photo-detail'),
]
