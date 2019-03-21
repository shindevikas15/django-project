from django.contrib import admin
from webapp.models import EmpFresher
from webapp.models import EmpProfessional



# Register your models here.


class EmpFresherAdmin(admin.ModelAdmin):
    list_display = ['name','Email_ID','phone_number','location',]
admin.site.register(EmpFresher,EmpFresherAdmin)


class EmpProfessionalAdmin(admin.ModelAdmin):
    list_display = ['name','Email_ID','phone_number','location']
admin.site.register(EmpProfessional,EmpProfessionalAdmin)