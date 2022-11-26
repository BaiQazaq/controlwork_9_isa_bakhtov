from django.urls import path

from photos.views.photo_create_view import PhotoCreate
from photos.views.photos_list_view import PhotoView
from photos.views.photo_detail_view import PhotoDetailView
from photos.views.photo_delete_view import PhotoDeleteView
from photos.views.photo_update_view import PhotoUpdateView


urlpatterns = [
    path("", PhotoView.as_view(), name='index'),
    path("photo/add/", PhotoCreate.as_view(), name='photo_creation'),
    path("photo/<int:pk>/detail", PhotoDetailView.as_view(), name='photo_detail'),
    path("photo/<int:pk>/update", PhotoUpdateView.as_view(), name='photo_update'),
    path("photo/<int:pk>/delete/", PhotoDeleteView.as_view(), name= "photo_delete"),
    path("photo/<int:pk>/confirm_delete/", PhotoDeleteView.as_view(), name= "confirm_delete"),
]