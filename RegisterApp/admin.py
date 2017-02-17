from django.contrib import admin
from RegisterApp.models import Register

# Register your models here.


class RegisterModelAdmin(admin.ModelAdmin):
	list_display=["name","email","phone_number","registd_date"]
	list_filter=["registd_date"]
	search_fields=["name","email","phone_number","events"]
	class Meta:
		model = Register



admin.site.register(Register,RegisterModelAdmin)