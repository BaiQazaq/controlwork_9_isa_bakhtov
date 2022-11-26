from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


from photos.models import Photo

# class GroupPermission(UserPassesTestMixin):
#     groups = []
    
#     def test_func(self):
#         return self.request.user.groups.filter(name__in=self.groups).exists()

class PhotoDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    template_name = 'photo_confirm_delete.html'
    model = Photo
    success_url = reverse_lazy('index')
    # groups = ['admin', "user"]
    permission_required = 'photos.can_delete_photo'
    
    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user