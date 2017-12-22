from django.core.exceptions import ValidationError

GENDER = ['Male','Female']

def validate_gender(value):
	gen = value.capitalize()
	if not value in GENDER and not gen in GENDER:
		raise ValidationError("{value} not a valid gender") 
	return value

YEAR= ['1','2','3','4','5']

def validate_year(value):
	year = value.capitalize()
	if not value in YEAR and not year in YEAR:
		raise ValidationError("{value} not a valid year") 
	return value