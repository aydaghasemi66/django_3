from django import forms
from .models import *





class NewsLetterForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = ['email']

class ContactUsForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = ['name', 'email','subject', 'message']
class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ['name','email','phone','date','department','doctor', 'message',]

