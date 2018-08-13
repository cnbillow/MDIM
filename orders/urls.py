from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    url(r'^basket_adding/$', basket_adding, name='basket_adding'),
    url(r'^checkout/$', checkout, name='checkout'),
]
