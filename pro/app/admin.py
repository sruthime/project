from django.contrib import admin
from .models import Departments,Faculty,Appointment
# Register your models here.
admin.site.register(Departments)
admin.site.register(Faculty)

class appadmin(admin.ModelAdmin):
    list_display=('id','Name','Email','PhoneNo','Department')



admin.site.register(Appointment,appadmin)


