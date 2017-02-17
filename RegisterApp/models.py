from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
from multiselectfield import MultiSelectField
# Create your models here.

class Register(models.Model):

	person_choice =((1,"Mad-Arts"),
			(2,"Football"),
			(3,"Cricket"),
			(4,"Treasure-Hunt"),
			(5,"Mr&Ms.Furore"),
			(6,"Group-Dance"),
			(7,"JAM"),
            (8, "Sketching"))
	name = models.CharField(max_length=100)
	email= models.EmailField(max_length=100)
	phone_regex = RegexValidator(regex=r'^\d{10,10}$', message="Enter Valid Phone Number (10-digits)")
	phone_number = models.CharField(max_length=10,validators=[phone_regex])
	registd_date = models.DateTimeField(auto_now_add=True)
	events = MultiSelectField(choices=person_choice,default=None)


	def __str__(self):
		return self.name

