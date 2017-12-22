# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView
	)

from .models import Course

from .forms import CourseCreateForm

# Create your views here.

class CourseListView(ListView):
	def get_queryset(self):
		return Course.objects.filter(user=self.request.user)


class CourseDetailView(DetailView):
	def get_queryset(self):
		return Course.objects.filter(user=self.request.user)

class CourseCreateView(CreateView):
	form_class = CourseCreateForm
	template_name = 'form.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(CourseCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(CourseCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Course'
		return context

class CourseUpdateView(UpdateView):
	form_class = CourseCreateForm
	template_name = 'courses/detail-update.html'

	def get_queryset(self):
		return Course.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(CourseUpdateView, self).get_context_data(*args, **kwargs)
		course_name = self.get_object().course_name
		context['title'] = 'Update Course:%s'% course_name
		return context