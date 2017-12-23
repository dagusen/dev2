from django.conf.urls import url

from .views import (
	PartylistListView,
	PartylistDetailView,
	PartyListCreateView
	)

urlpatterns = [
	url(r'^$', PartylistListView.as_view(), name='list'),
	url(r'^create/$', PartyListCreateView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', PartylistDetailView.as_view(), name='detail')
]