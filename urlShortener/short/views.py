from django.shortcuts import redirect, render,get_object_or_404
from .forms import UrlShortenForm
from .models import Url
import short_url

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = UrlShortenForm(request.POST)
        if form.is_valid:
            url=form.save()
            url.shortened_url=short_url.encode_url(6)
            url.save()
            return redirect('index')
    elif request.method == 'GET':
        form = UrlShortenForm()
        urls= Url.objects.all()
        print(urls)
        data = {'form': form, 'urls':urls}
        return render(request, 'index.html', data)

def show(request, urlstring):
    print(urlstring)
    url=get_object_or_404(Url, shortened_url=urlstring)
    return redirect(url.url_string)