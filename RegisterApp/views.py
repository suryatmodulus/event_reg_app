from django.shortcuts import render,redirect
from RegisterApp.forms import RegForm,LoginForm
from RegisterApp.models import Register
from django.contrib.auth import authenticate,login,logout
from RegisterApp.Sms_Api import Send_Sms
#from RegisterApp.way2sms_3 import Send_OTP
from RegisterApp.SG_Email import Send_Email
from RegisterApp.G_Sheets import Update_GS

# Create your views here.

#passwd="20130877274"

org_email_dic={"1":"suryatmodulus@gmail.com"}

def LoginView(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username , password=password)
		login(request,user)
		return redirect("/register")
	return render(request,"login1.html")


# def RegView(request):
# 	if request.user.is_authenticated():
# 		username=request.user.username
# 		form = RegForm(request.POST or None)
# 		if form.is_valid():
# 			name=form.cleaned_data.get("name")
# 			email = form.cleaned_data.get("email")
# 			number=form.cleaned_data.get("phone_number")
# 			event_items=form.cleaned_data.get("events")
# 			amount=form.cleaned_data.get("amount")
# 			rand_id=random.randrange(10000,99999)
# 			qr_value="dscef17"+str(int(int(number)/rand_id))+name[:3]
# 			print(username+" : "+qr_value)
# 			request.session['qr_key'] = qr_value
# 			conf_message="Hey "+str(name.title())+", Furore'17 Registration Successful! "+"Download QR-code @ "+"http://api.qrserver.com/v1/create-qr-code/?data="+str(qr_value)
# 			for event in event_items:
# 				try:
# 					org_email=org_email_dic[event]
# 					org_message="Reg-Name : "+str(name.title())+" || Reg-No : "+str(number)+" || Reg-Id : "+str(qr_value)
# 					Send_Email(org_email,org_message)

# 				except:
# 					pass
# 			Send_Email(email,conf_message)
# 			try:
# 				#Send_OTP(username,passwd,conf_message,number)
# 				Send_Sms(number,conf_message)
# 			except:
# 				pass
# 			form.save()
# 			Register.objects.filter(name=name,email=email,amount=amount).update(reg_id=qr_value)
# 			return redirect("/success")
# 		return render(request,"register.html",{})
# 	return redirect("/")

# def SuccessView(request):
# 	if request.user.is_authenticated():
# 		qr_id = request.session['qr_key']
# 	   	return render(request,"success.html",{"qr_id":qr_id})
# 	return redirect("/")

def RegView(request):
	if request.user.is_authenticated():
		username=request.user.username
		form = RegForm(request.POST or None)
		if form.is_valid():
			name=form.cleaned_data.get("name")
			email = form.cleaned_data.get("email")
			phone_no=form.cleaned_data.get("phone_no")
			college_name=form.cleaned_data.get("college_name")
			ticket_no=form.cleaned_data.get("ticket_no")
			ticket_cat = form.cleaned_data.get("ticket_cat")
			reg_by = form.cleaned_data.get("reg_by")
			form.save()
			Update_GS("QWRegistrations",[name,email,phone_no,college_name,ticket_no,ticket_cat,reg_by])
			return redirect("/success")
		return render(request,"register1.html",{"user":request.user.username})
	return redirect("/")

def SuccessView(request):
	if request.user.is_authenticated():
		return render(request,"success1.html",{})
	return redirect("/")

def LogoutView(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect("/")


#-----------------------------
# To send event list

#event_list=[]
			#for item in event_items:
				#value=event_dic[item]
				#event_list.append(value)
			#event_list=",".join(event_list) """