from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.views.generic import  DetailView
from photos.models import Photo, Choice
# from accounts.forms import SubsForm



class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0
        
        
    def get_context_data(self,object_list=None, **kwargs):
        context = super(ProfileView, self).get_context_data(object_list=object_list, **kwargs)
        author = self.get_object()
        
        photos_choosed = Choice.objects.filter(liked_by=author.pk)
        
        photos = []
        for i in photos_choosed:
            photo = Photo.objects.filter(id=i.id)
            photos.append(photo)
        kwargs['photos'] = photos
        print("+++++", kwargs['photos'])
        paginator = Paginator(photos, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        # kwargs['photos'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs, context=context)


        
        
    # def get_context_data(self, **kwargs):
    #     vacancies = self.get_object().vacancies_view.all()
    #     paginator = Paginator(vacancies, self.paginate_related_by, orphans=self.paginate_related_orphans)
    #     page_number = self.request.GET.get('page', 1)
    #     page = paginator.get_page(page_number)
    #     kwargs['page_obj'] = page
    #     kwargs['vacancies'] = page.object_list
    #     kwargs['is_paginated'] = page.has_other_pages()
    #     return super().get_context_data(**kwargs)
