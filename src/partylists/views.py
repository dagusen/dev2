# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.conf import settings

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import PartyList

User = settings.AUTH_USER_MODEL

# Create your views here.

class PartylistListView(ListView):
	def get_queryset(self):
		return PartyList.objects.filter(user=self.request.user)

class PartylistDetailView(DetailView):
	def get_queryset(self):
		return PartyList.objects.filter(user=self.request.user)