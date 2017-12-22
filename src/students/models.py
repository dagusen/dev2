# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import pre_save

from django.core.urlresolvers import reverse

from django.conf import settings

from departments.models import unique_slug_generator

from .validators import validate_gender, validate_year

from courses.models import Course

User = settings.AUTH_USER_MODEL

# Create your models here.

Year = (
    	('1', '1st year'),
    	('2', '2nd year'),
    	('3', '3rd year'),
    	('4', '4th year'),
    	('5', '5th year'),
    )

Gender = (
		('Female', 'Female'),
        ('Male', 'Male'),
    )

class Student(models.Model):
	user 				= models.ForeignKey(User)
	first_name 			= models.CharField(max_length=120)
	middle_name 		= models.CharField(max_length=120)
	last_name 			= models.CharField(max_length=120)
	gender 				= models.CharField(max_length=10, choices=Gender, help_text='Select your gender', validators=[validate_gender])
	age 				= models.IntegerField()
	course 				= models.ForeignKey(Course, on_delete=models.CASCADE)
	year 				= models.CharField(max_length=1, choices=Year, help_text='Select your year', validators=[validate_year])
	timestamp			= models.DateTimeField(auto_now_add=True)
 	updated				= models.DateTimeField(auto_now=True)
 	slug				= models.SlugField(null=True, blank=True)

	def __str__(self):
		return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

	def get_absolute_url(self):
	  	return reverse('students:edit', kwargs={'slug': self.slug})

	@property
	def title(self):
		return self.first_name

def rl_pre_save_receiver(sender, instance, *arg, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Student)