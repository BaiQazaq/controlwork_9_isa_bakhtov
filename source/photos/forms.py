from django import forms

from photos.models import Photo, Choice



class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('image', 'sign')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Search')
    

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['mark']
        