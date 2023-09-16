from django.shortcuts import render,redirect
from .forms import CustomUserCreation,UpdateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomeUser
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        form = AuthenticationForm()
        return render(request,'registration/login.html', context={'form': form})
    elif request.method == 'POST':
        if '@' in request.POST.get('username'):
            try:
                username = CustomeUser.objects.get(email=request.POST.get('username').strip()).username
            except:
                messages.add_message(request, messages.ERROR, 'Invalid username or password')
                return redirect(request.path_info)
        else:
            username = request.POST.get('username').strip()
        password = request.POST.get('password')      
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid username or password')
            return redirect(request.path_info)

@login_required
def Logout(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        form = CustomUserCreation()
        return render(request,'registration/signup.html', context={'form': form})
    else:
        form = CustomUserCreation(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid username or password')
                return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, 'Invalid username or password')
            return redirect(request.path_info)
        
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(request.path_info)  # Redirect to the user's profile page or the appropriate URL
    else:
        user_form = UpdateUserForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'user_form': user_form})

