from django.shortcuts import render,redirect
from RegisterApp.forms import RegForm,LoginForm
from RegisterApp.models import Register
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def LoginView(request):
	nav_option="Know me ?"
	nav_href="about"
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username , password=password)
		login(request,user)
		return redirect("/register")
	return render(request,"login.html",{})


def RegView(request):
	if request.user.is_authenticated():
		form = RegForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect("/success")
		return render(request,"register.html",{})
	return redirect("/")

def SuccessView(request):
	if request.user.is_authenticated():
		return render(request,"success.html",{})
	return redirect("/")
