# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

# Create your models here.

class Department(models.Model):
	owner					= models.ForeignKey(User)
	department_name			= models.CharField(max_length=120)
	department_code			= models.CharField(max_length=120, null=True, blank=True)
	department_dean			= models.CharField(max_length=120, null=True, blank=True)
	timestamp				= models.DateTimeField(auto_now_add=True)
	updated					= models.DateTimeField(auto_now=True)
	slug					= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.name


	@property
	def title(self):
		return self.department_name