from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings



# Create your models here.



class Services (models.Model):
    title = models.CharField(max_length=200)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    content = models.TextField()


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_data']



class ContactUs(models.Model):
    message = models.TextField()
    email = models.EmailField()
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)


    def __str__(self):
        return self.name 
    
class NewsLetter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Job(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class Doctor(models.Model):
    info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctors', default='user.png')
    twitter = models.CharField(max_length=255, default='#')
    facebook = models.CharField(max_length=255, default='#')
    instagram = models.CharField(max_length=255, default='#')
    linkdin = models.CharField(max_length=255, default='#')
    status = models.BooleanField(default=False)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.username
    
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    message = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Testimonials(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment=models.TextField()
    job=models.CharField(max_length=100)
    image=models.ImageField(upload_to='testimonials',default='user.png')
    def __str__(self):
        return self.user.username

