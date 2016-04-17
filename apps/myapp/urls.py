from django.conf.urls import url

from .views import ItemCreateView, ItemDetailView
from .models import Item

urlpatterns = [
    url(r'^create$', ItemCreateView.as_view(), name='item-creation'),
    url(r'^item/(?P<pk>[0-9]+)/$', ItemDetailView.as_view(), name='item-detail'),
]