from django.shortcuts import render
from FirstApp.forms import MoviesForm
from django.http import HttpResponse
# Create your views here.

def reg(request):
	if request.method=='POST':
		form=MoviesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Done")
	form=MoviesForm()
	return render(request,'register.html',{'form':form})
