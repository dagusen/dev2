from django.conf.urls import url

from .views import (
	DepartmentListView,
	DepartmentDetailView,
	DepartmentUpdateView,
	DepartmentCreateView
	)

urlpatterns = [
	url(r'^$', DepartmentListView.as_view(), name='list'),
	url(r'^create/$', DepartmentCreateView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', DepartmentUpdateView.as_view(), name='detail')
]