from django.urls import path

from messageapp.views import index


urlpatterns = [
    path('', index),
]