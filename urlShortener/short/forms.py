from django import forms
from .models import Url


class UrlShortenForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['url_string']
        # widgets = {'urlString': forms.URLField()}
