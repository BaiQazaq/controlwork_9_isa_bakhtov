from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from photos.models import Choice, Photo
from photos.forms import ChoiceForm




class ChoiceView(LoginRequiredMixin, CreateView):
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('index')

    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        liked_by = self.request.user
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            mark = form.cleaned_data.get('mark')
            if not Choice.objects.filter(photo=photo, liked_by=liked_by, mark=mark).exists():
                Choice.objects.create(photo=photo, liked_by=liked_by, mark=mark)
        else:
            form = {'text' : 'Somthing wrong did not choice'}
        return redirect('index')



    
    

