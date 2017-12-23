from django.conf.urls import url

from .views import (
	PartylistListView,
	PartylistDetailView
	)

urlpatterns = [
	url(r'^$', PartylistListView.as_view(), name='list'),
	# url(r'^create/$', StudentCreateView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', PartylistDetailView.as_view(), name='detail')
]