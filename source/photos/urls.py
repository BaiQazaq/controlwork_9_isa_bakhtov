from django.urls import path

from photos.views.photo_create_view import PhotoCreate
from photos.views.photos_list_view import PhotoView
from photos.views.photo_detail_view import PhotoDetailView
from photos.views.photo_delete_view import PhotoDeleteView
from photos.views.photo_update_view import PhotoUpdateView


urlpatterns = [
    path("", PhotoView.as_view(), name='index'),
    path("add/", PhotoCreate.as_view(), name='photo_creation'),
    path("detail/<int:pk>", PhotoDetailView.as_view(), name='photo_detail'),
    path("update/<int:pk>", PhotoUpdateView.as_view(), name='photo_update'),
    path("photo/<int:pk>/delete/", PhotoDeleteView.as_view(), name= "photo_delete"),
    path("photo/<int:pk>/confirm_delete/", PhotoDeleteView.as_view(), name= "confirm_delete"),
]