from django.conf.urls import url

from .views import (
	PartylistListView,
	PartylistDetailView,
	PartyListCreateView,
	PartyListUpdateView
	)

urlpatterns = [
	url(r'^$', PartylistListView.as_view(), name='list'),
	url(r'^create/$', PartyListCreateView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', PartyListUpdateView.as_view(), name='edit')
]