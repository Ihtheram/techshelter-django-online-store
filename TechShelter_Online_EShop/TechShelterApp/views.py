from django.shortcuts import render, redirect

from .models import User

from TechShelterApp.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
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