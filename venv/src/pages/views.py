from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
	return HttpResponse("<h1>Hello World</h1>") # string of html code, not actual html code

def contact_view(*args, **kwargs):
	return HttpResponse("<h1>This is a contact view</h1>") 