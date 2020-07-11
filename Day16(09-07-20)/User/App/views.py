from django.shortcuts import render
from App.forms import MyForm
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
	if request.method=='POST':
		data=MyForm(request.POST)
		if data.is_valid():
			data.save()
			return HttpResponse("<h1>Registered Successfully")

	form=MyForm()
	return render(request,'register.html',{'form':form})

def home(request):

	return render(request,'home.html')
	

@login_required
def profile(request):
	data=User.objects.all()
	return render(request,'profile.html',{'data':data})