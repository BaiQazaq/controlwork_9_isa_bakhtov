from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

from photos.models import Photo
from photos.forms import PhotoForm


class PhotoCreate(LoginRequiredMixin, CreateView):
    template_name = 'photo_create.html'
    form_class = PhotoForm
    model = Photo
    
    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)

        if form.is_valid():
            sign = form.cleaned_data.get('sign')
            image = form.cleaned_data.get('image')
            author = request.user
            if not Photo.objects.filter(sign=sign).exists():
                post = Photo.objects.create(sign=sign, image=image, author=author)
        else:
            form = {'text' : 'Smth went wrong, photo did not added'}
        return redirect('index')
    
    
    def get_success_url(self):
        return reverse_lazy('index')
    