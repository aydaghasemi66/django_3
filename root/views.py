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
        doctor_count = Doctor.objects.all().count()
        department_count = Department.objects.all().count()
        service_count=Services.objects.all().count()
        context = {
            'services':services,
            'department':department,
            'doctor':doctor,
            'dec' : department_count,
            'dc': doctor_count,
            'sc': service_count,
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
        
    elif request.method == 'POST' and len(request.POST) == 5:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'We received your message')
        else:
            messages.add_message(request, messages.ERROR, 'invalid data')
        return redirect('root:home')
    elif request.method == 'POST' and len(request.POST) == 8:
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'submited')
        else:
            messages.add_message(request, messages.ERROR, 'invalid data')
        return redirect('root:home')


