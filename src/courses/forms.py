from django import forms

from .models import Course

class CourseCreateForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = [
			'department',
			'course_name',
			'course_code'
		]