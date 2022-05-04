from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:urlstring>', views.show, name='show'),
]
