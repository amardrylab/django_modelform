from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import AuthorForm

# Create your views here.


class AuthorCreate(CreateView):
	form_class=AuthorForm
	template_name='author_create.html'
