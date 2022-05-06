from django.urls import path
from . import views
from django.urls import re_path as url

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^lumbers/$', views.LumberListView.as_view(), name='lumber'),
    url(r'^lumbers/(?P<pk>\d+)$', views.LumberDetailView.as_view(), name='lumber-detail'),
    url(r'^types/$', views.TypeListView.as_view(), name='types'),
    url(r'^types/(?P<pk>\d+)$', views.TypeDetailView.as_view(), name='type-detail'),

    url(r'^cement/$', views.CementListView.as_view(), name='cement'),
    url(r'^cement/(?P<pk>\d+)$', views.CementDetailView.as_view(), name='cement-detail'),
    url(r'^stamp_cement/$', views.StampCementListView.as_view(), name='stamp_cement'),
    url(r'^stamp_cement/(?P<pk>\d+)$', views.StampCementDetailView.as_view(), name='stamp_cement-detail'),

    url(r'^metal/$', views.MetalListView.as_view(), name='metal'),
    url(r'^metal/(?P<pk>\d+)$', views.MetalDetailView.as_view(), name='metal-detail'),
    url(r'^stamp_metal/$', views.StampMetalListView.as_view(), name='stamp_metal'),
    url(r'^stamp_metal/(?P<pk>\d+)$', views.StampMetalDetailView.as_view(), name='stamp_metal-detail'),
]
