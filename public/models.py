from django.db import models
from datetime import datetime 

# Create your models here.
class teacher_join(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=10)
    qualification=models.CharField(max_length=50)
    post=models.CharField(max_length=30)
    experience=models.CharField(max_length=15)
    last_school=models.CharField(max_length=50)
    date=models.DateTimeField(default=datetime.now())
    
class student_join(models.Model):
    
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    father_name=models.CharField(max_length=30)
    mother_name=models.CharField(max_length=30)
    father_email=models.CharField(max_length=30)
    father_contact=models.CharField(max_length=10)
    mother_email=models.CharField(max_length=30)
    mother_contact=models.CharField(max_length=10)
    date=models.DateTimeField(default=datetime.now())

class login_admin(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class alumni(models.Model):
    name=models.CharField(max_length=30)
    pass_out=models.CharField(max_length=15)
    job=models.CharField(max_length=30)
    discription=models.TextField()
    image=models.FileField()
    url=models.CharField(max_length=1500)
     

class achivement(models.Model):
    name=models.CharField(max_length=30)
    achive=models.CharField(max_length=50)
    discription=models.TextField()
    image=models.FileField()
    url=models.CharField(max_length=1500)    
     

class event(models.Model):
    image=models.FileField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500) 
class facility(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    url=models.CharField(max_length=1500)

class management(models.Model):
    image=models.FileField()
    name=models.CharField(max_length=50)
    discription=models.TextField()
    designation=models.CharField(max_length=20)
    url=models.CharField(max_length=1500)