from django.shortcuts import render, redirect

from .models import User

from TechShelterApp.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponse, Http404

from django.contrib.auth import get_user_model
User = get_user_model()

def tech_shelter(request):

    if request.user.is_authenticated:
        user = request.user        
    else:
        user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
       
    context = {'user':user}
    return render(request, 'TechShelterApp/tech_shelter.html',context)



def signup(request):

    if request.user.is_authenticated:
        user=request.user

    else:
        user = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
		}

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('TechShelterApp/tech_shelter.html')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/signup.html', {
			'user': user,'form':form
	    })

def logout(request):
    logout(request)
    return HttpResponse('TechShelterApp/tech_shelter.html')

def users(request):

    if request.user.is_superuser:
        users = User.objects.all()       
    else:
        users = {}
       
    context = {'users':users}
    return render(request, 'TechShelterApp/users.html',context)

def editprofile(request):
    form = UserForm()
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        #to see what info are input, in console, uncomment the line below
        #print('Printing POST:', request.POST)
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    
    if request.method == 'FILES':
        #to see what info are input, in console, uncomment the line below
        #print('Printing POST:', request.POST)
        form = UserForm(request.FILES, instance=user)
        if form.is_valid():
            form.update()
    
    context = {'form':form, 'user':user}
    return render(request, 'TechShelterApp/editprofile.html',context)