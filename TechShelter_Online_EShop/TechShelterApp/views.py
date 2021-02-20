from django.shortcuts import render, redirect

from .models import User

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def tech_shelter(request):

    if request.user.is_authenticated:
        user=request.user
        
    else:
        user = {
			'name':'guest',
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tech_shelter')
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {
			'user': user,'form':form
	    })