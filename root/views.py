from django.shortcuts import render , redirect
from accounts.models import CustomeUser
from django.contrib import messages
from .models import *
from .forms import *



# Create your views here.



def home (request):
    if request.method =='GET':
        services = Services.objects.filter(status=True)
        department=Department.objects.all()
        doctor=Doctor.objects.all()
        context = {
            'services':services,
            'department':department,
            'doctor':doctor,
        }

        return render(request,"root/index.html" , context=context)   
    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'Submited')
            return redirect('root:home')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid')
            return redirect('root:home')
        
    if request.method == 'POST' and len(request.POST) > 2:
        form2 = ContactUsForm(request.POST)
        if form2.is_valid():
            form2.save()
            messages.add_message(request, messages.SUCCESS, 'We received your message')
        else:
            messages.add_message(request, messages.ERROR, 'invalid data')
        return redirect('root:home')
    
def appointment(request):
    if request.method == 'GET':
        services = Services.objects.filter(status=True)
        department=Department.objects.all()
        doctor=Doctor.objects.all()
        context = {
            'services':services,
            'department':department,
            'doctor':doctor,
        }

        return render(request,"index.html",context=context)   

    elif request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment request submitted successfully.')
            return redirect('root:home')
        else:
            print(form.errors)
            messages.error(request, 'Invalid data. Please check the form fields.')
            return redirect('root:home')


