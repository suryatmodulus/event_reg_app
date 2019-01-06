from django.contrib import admin
from RegisterApp.models import Register

events_dic={'1':'Photography','2': 'Short-movie', '3': 'Sketching', '4': 'Painting', '5': 'Campus-Painting',
'6':'Crafts\Installation', '7': 'No-Idea', '8': 'Face-Painting', '9': 'Solo-Dance', '10': 'Tapang', '11': 'Western-Group',
'12':'Indian-Group', '13': 'Debate', '14': 'JAM', '15': 'Series-of-Unfortunate','16': 'Quiz(Genreal)','17': 'Pulp-Fiction',
'18':'Battle-of-Bands', '19': 'Instrumental-Solo', '20': 'Western-Vox-Solo', '21': 'Bollywood-Vox-Solo', '22': 'Classical-Vox-Solo',
'23': 'Mad-Ads', '24': 'Street-Paly', '25': 'Mono-Acting', '26': 'Pot-Pourri', '27': 'Standup-Comdey', '28': 'Fashion-Show',
'29': 'Mr-&-Mrs-Atlantis', '30': 'Crime-Connect-2.0', '31': 'Fifa-Auction', '32': 'Mini-Militia', '33': 'DSI-Minute',
'34': 'GoT-Quiz','35':'Carrom', '36': 'Treasure-Hunt', '37': 'Beat-Boxing', '38': 'Chuck-Glider', '39': 'Code-Golfing',
'40': 'Corporate-Roadies', '41':'Tech-DC-and-Pictonary', '42': 'Ideathon', '43': 'Tech-Treasure-Hunt', '44': 'Away-We -Go',
'45': 'Shark-Tank','46': 'Kinet-Sports', '47': 'Test-Your-Senses', '48': 'Funk-from-Junk', '49': 'Event-Selfie', '50': 'Futsal',
'51': 'Squash', '52': 'Basketball','53': 'Cricket', '54': 'Perspective'}

# class RegisterModelAdmin(admin.ModelAdmin):

# 	list_display=["name","email","phone_number","reg_id","amount","events_list"]

# 	def events_list(self, obj):
# 		selected_events_list=[]
# 		raw_events_list=obj.events
# 		for item in raw_events_list:
# 			selected_events_list.append(events_dic[item])
# 		return list(selected_events_list)


# 	search_fields=["name","events","email","phone_number","reg_id","amount"]

# 	class Meta:
# 		model = Register

class RegisterModelAdmin(admin.ModelAdmin):

	list_display=["name","email","phone_no","college_name","ticket_no","ticket_cat","reg_by"]
	search_fields=["name","email","phone_no","college_name","ticket_no","ticket_cat","reg_by"]

	class Meta:
		model = Register



admin.site.register(Register,RegisterModelAdmin)