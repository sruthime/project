from django.db import models

# Create your models here.
class Departments(models.Model):
    depName= models.CharField(max_length=25)
    description=models.TextField()

    def __str__(self):
        return self.depName

class Faculty(models.Model):
    fname=models.CharField(max_length=20)
    depart=models.ForeignKey(Departments,on_delete=models.CASCADE) 

   
    
class Appointment(models.Model):
    Name=models.CharField(max_length=200)  
    Email=models.EmailField(max_length=200)
    PhoneNo=models.CharField(max_length=50,null=True,blank=True)
    Department=models.ForeignKey(Departments,on_delete=models.CASCADE,null=True,blank=True)
    
    
   