from django.conf.urls import url
from . import views

__author__ = 'eddmash'

urlpatterns = [
    url(r"^page/add", views.PageCreateView.as_view(), name="page-new"),
    url(r"^page/(?P<slug>[0-9A-Za-z_\-]+)", views.PageUpdateView.as_view(), name="page-edit"),
    url(r"^page/(?P<slug>[0-9A-Za-z_\-]+)/delete$", views.PageListView.as_view(), name="page-delete"),
    url(r"^pages", views.PageListView.as_view(), name="pages"), 
]