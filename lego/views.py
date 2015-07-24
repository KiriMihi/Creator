from django.shortcuts import render

def home(request):
	return render(request, 'bootstrap/allauth/account/index.html')

def profile(request):
	return render(request, 'bootstrap/allauth/account/profile.html')