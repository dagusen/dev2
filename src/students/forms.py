from django import forms

from .models import Student

class StudentCreateForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
			'first_name',
			'middle_name',
			'last_name',
			'gender',
			'age',
			'course',
			'year'
		]