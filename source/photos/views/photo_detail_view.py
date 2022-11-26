from django.views.generic import DetailView
# from urllib.parse import urlencode

from photos.models import Photo


class PhotoDetailView(DetailView):
    template_name = 'photo_detail.html'
    model =  Photo
    pk_url_kwarg = 'pk'
    context_object_name = 'photo'
    
    
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(PhotoDetailView, self).get_context_data(object_list=object_list, **kwargs)
    #     photo = self.object
    #     return context
    
    