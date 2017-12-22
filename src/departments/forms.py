from django import forms

from .models import Department

class DepartmentCreateForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = [
			'department_name',
			'department_code',
			'department_dean'
		]