from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from django.utils import timezone

# Create your models here.
# class Register(models.Model):

# 	person_choice =((1,"Photography"),
# 			(2,"Short-movie"),
# 			(3,"Sketching"),
# 			(4,"Painting"),
# 			(5,"Campus-Painting"),
# 			(6,"Crafts\Installation"),
# 			(7,"No-Idea"),
#             (8,"Face-Painting"),
#             (9,"Solo-Dance"),
# 			(10,"Tapang"),
# 			(11,"Western-Group"),
# 			(12,"Indian-Group"),
# 			(13,"Debate"),
# 			(14,"JAM"),
# 			(15,"Series-of-Unfortunate"),
#             (16,"Quiz(Genreal)"),
#             (17,"Pulp-Fiction"),
# 			(18,"Battle-of-Bands"),
# 			(19,"Instrumental-Solo"),
# 			(20,"Western-Vox-Solo"),
# 			(21,"Bollywood-Vox-Solo"),
# 			(22,"Classical-Vox-Solo"),
# 			(23,"Mad-Ads"),
#             (24,"Street-Paly"),
#             (25,"Mono-Acting"),
# 			(26,"Pot-Pourri"),
# 			(27,"Standup-Comdey"),
# 			(28,"Fashion-Show"),
# 			(29,"Mr-&-Mrs-Atlantis"),
# 			(30,"Crime-Connect-2.0"),
# 			(31,"Fifa-Auction"),
#             (32,"Mini-Militia"),
#             (33,"DSI-Minute"),
# 			(34,"GoT-Quiz"),
# 			(35,"Carrom"),
# 			(36,"Treasure-Hunt"),
# 			(37,"Beat-Boxing"),
#             (38,"Chuck-Glider"),
#             (39,"Code-Golfing"),
# 			(40,"Corporate-Roadies"),
# 			(41,"Tech-DC-and-Pictonary"),
# 			(42,"Ideathon"),
# 			(43,"Tech-Treasure-Hunt"),
#             (44,"Away-We -Go"),
#             (45,"Shark-Tank"),
# 			(46,"Kinet-Sports"),
# 			(47,"Test-Your-Senses"),
# 			(48,"Funk-from-Junk"),
# 			(49,"Event-Selfie"),
#             (50,"Futsal"),
#             (51,"Squash"),
# 			(52,"Basketball"),
# 			(53,"Cricket"),
# 			(54,"Perspective"))

# 	name = models.CharField(max_length=100)
# 	email= models.EmailField(max_length=100)
# 	phone_regex = RegexValidator(regex=r'^\d{10,10}$', message="Enter Valid Phone Number (10-digits)")
# 	phone_number = models.CharField(max_length=10,validators=[phone_regex])
# 	registd_date = models.DateTimeField(default=timezone.now)
# 	events = MultiSelectField(choices=person_choice,default=None)
# 	amount = models.IntegerField(default=0)
# 	reg_id = models.CharField(max_length=100,default=0)

class Register(models.Model):

	name = models.CharField(max_length=100)
	email= models.EmailField(max_length=100)
	phone_regex = RegexValidator(regex=r'^\d{10,10}$', message="Enter Valid Phone Number (10-digits)")
	phone_no = models.CharField(max_length=10,validators=[phone_regex])
	college_name = models.CharField(max_length=150)
	ticket_no = models.CharField(max_length=5,default=0)
	ticket_cat = models.CharField(max_length=15)
	reg_by = models.CharField(max_length=100)
	reg_date = models.DateTimeField(default=timezone.now)



	def __str__(self):
		return self.name

