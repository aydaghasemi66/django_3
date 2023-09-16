from django import forms
from .models import CustomeUser
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser

class CustomUserCreation(UserCreationForm):

    class Meta:
        model = CustomeUser
        fields = ['username', 'email', 'password1', 'password2','id_code', 'mobile','image']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_code=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile=forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class': 'form-control'}))
    image=forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomeUser
        fields = ['username', 'email','id_code','mobile','image']




