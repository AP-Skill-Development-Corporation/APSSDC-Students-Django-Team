from django.shortcuts import render
from FirstApp.forms import ChangeForm
from django.http import HttpResponse
from FirstApp.models import Change
from django.core.mail import send_mail
from ChangePwd import settings 
# Create your views here.
def register(request):
	if request.method=='POST':
		form=ChangeForm(request.POST)
		if form.is_valid():
			form.save()
			sub="Reg to Login Cradetials"
			body="Hello Your Username is:"+request.POST['username']+"Your Password is:"+request.POST['password']
			reciver=request.POST['mailid']
			sender=settings.EMAIL_HOST_USER
			send_mail(sub,body,sender,[reciver])
			return HttpResponse("<h1>Please check your Eamil for login details<h1>")

	form=ChangeForm()
	return render(request,'register.html',{'form':form})

def login(request):
	if request.method=='POST':
		uname=request.POST['username']
		pwd=request.POST['password']
		data=Change.objects.get(username=uname,password=pwd)
		if data:
			return render(request,'welcome.html',{'uname':uname})
		else:
			return HttpResponse("<h1>Invald User</h1>")

	return render(request,'login.html')


def forgotpwd(request):
	if request.method=='POST':
		data=Change.objects.get(mailid=request.POST['mail'])
		sub="Reg to Your Login details...!"
		body="Username is: "+data.username+" password is: "+data.password
		sender=settings.EMAIL_HOST_USER
		reciver=request.POST['mail']
		send_mail(sub,body,sender,[reciver])
		return HttpResponse('<h1>Check Your Eamil for login details</h1>')
	return render(request,"forgotpwd.html")

def changepassword(request):
	if request.method=='POST':
		oldpass=request.POST['oldpass']
		newpass=request.POST['newpass']
		conpass=request.POST['conpass']
		data=Change.objects.get(password=oldpass)
		if newpass != conpass:
			return HttpResponse('Password Doest match')
		else:
			data.password=conpass
			data.save()
			return HttpResponse('Password Updated')

	return render(request,'changepassword.html')
