# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from django.conf import settings

from django.db import models

from django.db.models.signals import pre_save

from departments.utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

from departments.models import Department

# Create your models here.

class Course(models.Model):
	user 				= models.ForeignKey(User)
	department 			= models.ForeignKey(Department, on_delete=models.CASCADE)
	course_name 		= models.CharField(max_length=120)
	course_code 		= models.CharField(max_length=120)
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)
	slug				= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.course_name

	def get_absolute_url(self):
		return reverse('courses:edit', kwargs={'slug': self.slug})

	@property
	def title(self):
		return self.course_name

def rl_pre_save_receiver(sender, instance, *arg, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Course)
