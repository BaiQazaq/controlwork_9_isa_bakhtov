from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse

from photos.forms import PhotoForm
from photos.models import Photo


class GroupPermission(UserPassesTestMixin):
    groups = []
    
    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()

class PhotoUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'photo_update.html'
    form_class = PhotoForm
    model = Photo
    context_object_name = 'photo'
    groups = ['admin', 'user']  
    
    
    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})
