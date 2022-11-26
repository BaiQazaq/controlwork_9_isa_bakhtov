from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse

from photos.forms import PhotoForm
from photos.models import Photo


# class GroupPermission(UserPassesTestMixin):
#     groups = []
    
#     def test_func(self):
#         return self.request.user.groups.filter(name__in=self.groups).exists()

class PhotoUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):

    template_name = 'photo_update.html'
    form_class = PhotoForm
    model = Photo
    context_object_name = 'photo'
    # groups = ['admin', 'user'] 
    permission_required = 'photos.can_change_photo'
    
    
    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user
    
    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})
    
    
