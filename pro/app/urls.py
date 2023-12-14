from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about/",views.about,name='about'),
    path("appointment",views.appointment,name='appointment'),
    path("department/",views.department,name='department'),
    path("faculty",views.faculty,name='faculty')

]
