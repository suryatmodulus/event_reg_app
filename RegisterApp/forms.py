from django import forms
from django.forms import ModelForm
from RegisterApp.models import Register
from django.contrib.auth import authenticate



# Create your forms here.


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self , *args , **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username , password = password)
			if not user:
				raise forms.ValidationError("This user does not exist")
		return super(LoginForm , self).clean(*args,**kwargs)

class RegForm(ModelForm):
	class Meta:
		model= Register
		fields=["name","email","phone_no","college_name","ticket_no","ticket_cat","reg_by"]
