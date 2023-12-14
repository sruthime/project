from django.shortcuts import render
from .models import Departments,Faculty
from .forms import appform

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def appointment(request):
    if request.method=="POST":
        form=appform(request.POST)
        if form.is_valid():
            form.save()      
            return render(request,'confirmation.html')
    form=appform()
    dform={
        'form':form
    }
    return render(request,"appointment.html",dform)

def department(request):
    dep={
        'dept':Departments.objects.all()
    }
    return render(request,"dept.html",dep)

def faculty(request):
    fac={
        'fact':Faculty.objects.all()
    }
    return render(request,"faculty.html",fac)

