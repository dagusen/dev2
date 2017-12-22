# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Student

from .forms import StudentCreateForm

# Create your views here.

class StudentListView(ListView):
	def get_queryset(self):
		return Student.objects.filter(user=self.request.user)

class StudentDetailView(DetailView):
	def get_queryset(self):
		return Student.objects.filter(user=self.request.user)

class StudentCreateView(CreateView):
	form_class = StudentCreateForm
	template_name = 'form.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(StudentCreateView, self).form_valid(form)

	# context for html title
	def get_context_data(self, *args, **kwargs):
		context = super(StudentCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Student'
		return context

class StudentUpdateView(UpdateView):
	form_class = StudentCreateForm
	template_name = 'students/detail-update.html'

	def get_queryset(self):
		return Student.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(*args, **kwargs)
		first_name = self.get_object().first_name
		context['title'] = 'Update Department:%s'% first_name
		return context
