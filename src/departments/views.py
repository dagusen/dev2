# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Department

from .forms import DepartmentCreateForm

# Create your views here.

class DepartmentListView(ListView):
	def get_queryset(self):
		return Department.objects.filter(owner=self.request.user)

class DepartmentDetailView(DetailView):
	def get_queryset(self):
		return Department.objects.filter(owner=self.request.user)

class DepartmentCreateView(CreateView):
	form_class = DepartmentCreateForm
	template_name = 'form.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(DepartmentCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(DepartmentCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Department'
		return context

class DepartmentUpdateView(UpdateView):
	form_class = DepartmentCreateForm
	template_name = 'departments/detail-update.html'

	def get_context_data(self, *args, **kwargs):
		context = super(DepartmentUpdateView, self).get_context_data(*args, **kwargs)
		department_name = self.get_object().department_name
		context['title'] = 'Update Department:%s'% department_name
		return context

	def get_queryset(self):
		return Department.objects.filter(owner=self.request.user)