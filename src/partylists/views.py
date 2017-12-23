# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.conf import settings

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import PartyList

from .forms import PartyListCreateForm

User = settings.AUTH_USER_MODEL

# Create your views here.

class PartylistListView(ListView):
	def get_queryset(self):
		return PartyList.objects.filter(user=self.request.user)

class PartylistDetailView(DetailView):
	def get_queryset(self):
		return PartyList.objects.filter(user=self.request.user)

class PartyListCreateView(CreateView):
	form_class = PartyListCreateForm
	template_name = 'form.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(PartyListCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(PartyListCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Party List'
		return context

class PartyListUpdateView(UpdateView):
	form_class = PartyListCreateForm
	template_name = 'partylists/detail-update.html'

	# context for html title
	def get_context_data(self, *args, **kwargs):
		context = super(PartyListUpdateView, self).get_context_data(*args, **kwargs)
		partylist_name = self.get_object().partylist_name
		context['title'] = 'Update Party List:%s'% partylist_name
		return context

	def get_queryset(self):
		return PartyList.objects.filter(user=self.request.user)