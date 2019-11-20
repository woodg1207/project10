from django.urls import path
from . import views
appname='movies'
urlpatterns = [
    path('', views.index, name='index'),
]
