from django.conf.urls import url

from .views import (
	CourseListView,
	CourseDetailView,
	CourseCreateView,
	CourseUpdateView
	)

urlpatterns = [
	url(r'^$', CourseListView.as_view(), name='list'),
	url(r'^create/$', CourseCreateView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', CourseUpdateView.as_view(), name='edit')
]