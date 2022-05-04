from django.shortcuts import redirect, render
from .forms import UrlShortenForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = UrlShortenForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    elif request.method == 'GET':
        form = UrlShortenForm()
        data = {'form': form}
        return render(request, 'index.html', data)
