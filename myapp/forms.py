from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
	name=forms.CharField(label='Author', max_length=20)
	class Meta:
		model=Author
		fields=['name']
