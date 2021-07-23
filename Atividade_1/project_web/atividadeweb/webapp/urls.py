from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('home/', index),
    path('w3c/', w3c, name="w3c"),
    path('html/', html, name="html"),
    path('css/', css, name="css"),
    path('javascript/', javascript, name="javascript"),
    path('frontend/', frontend, name="frontend"),
    path('backend/', backend, name="backend"),
    path('contact/', contact, name="contact"),


]
