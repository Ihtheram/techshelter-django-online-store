from django.shortcuts import render, redirect

from .models import User, Tech, OrderInfo, OrderedTech

from TechShelterApp.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, UserUpdateForm, Admin_UserUpdateForm, TechForm, DeliveryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


import json
from django.http import JsonResponse, HttpResponse, Http404

from django.contrib.auth import get_user_model
from django.contrib import messages

def tech_shelter(request):

    techs = Tech.objects.all()

    if request.user.is_authenticated:
        logged_in_user = request.user
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()       
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []
    
    context = {'logged_in_user':logged_in_user, 'techs':techs, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
    return render(request, 'TechShelterApp/tech_shelter.html',context)

def devices(request):

    if request.user.is_authenticated:
        logged_in_user = request.user
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()       
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []

    techs = Tech.objects.filter(digital=False)
    context = {'logged_in_user':logged_in_user, 'techs':techs, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
    return render(request, 'TechShelterApp/tech_shelter.html',context)

def softwares(request):

    if request.user.is_authenticated:
        logged_in_user = request.user
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()       
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []

    techs = Tech.objects.filter(digital=True)
    context = {'logged_in_user':logged_in_user, 'techs':techs, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
    return render(request, 'TechShelterApp/tech_shelter.html',context)

def tech_detail(request, techID):

    if request.user.is_authenticated:
        logged_in_user = request.user
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()       
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []

    try:
        this_tech = Tech.objects.get(id=techID)
    except Tech.DoesNotExist:
        raise Http404("Tech does not exist")

    context = {'logged_in_user':logged_in_user, 'this_tech': this_tech, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
    return render(request, 'TechShelterApp/tech_detail.html',context)

def orders(request):

    if request.user.is_authenticated:
        logged_in_user = request.user 
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        items = orderinfo.orderedtech_set.all()
        orderedtechs = OrderedTech.objects.all()

        orderhistory = OrderInfo.objects.filter(customer=logged_in_user, complete=True)

    else:
        logged_in_user = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        items = []
        orderedtechs = []
        orderhistory = []
    context = {'logged_in_user':logged_in_user, 'items':items, 'orderedtechs':orderedtechs,'orderinfo':orderinfo, 'orderhistory':orderhistory}
    return render(request, 'TechShelterApp/orders.html',context)

def orders_received(request):

    if request.user.is_authenticated:
        logged_in_user = request.user 
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        items = orderinfo.orderedtech_set.all()
        orderedtechs = OrderedTech.objects.all()

        # ordered = OrderInfo.objects.get(complete=True)
        # mytechs = Tech.objects.get(seller=logged_in_user)
        # mytechsordered = OrderedTech.objects.filter(order=ordered, tech=mytechs)
        
        rcv_ord_quantity = 0
        for orderedtech in orderedtechs:
            if orderedtech.order.complete and orderedtech.tech.seller.username == logged_in_user.username:
                rcv_ord_quantity+=1



    else:
        logged_in_user = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        items = []
        orderedtechs = []
        rcv_ord_quantity = 0
    


    context = {'logged_in_user':logged_in_user, 'items':items, 'orderedtechs':orderedtechs,'orderinfo':orderinfo, 'rcv_ord_quantity':rcv_ord_quantity}
    return render(request, 'TechShelterApp/orders_rcv.html',context)

def cart(request):

    if request.user.is_authenticated:
        logged_in_user = request.user 
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()

    else:
        logged_in_user = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []
    
    context = {'logged_in_user':logged_in_user, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
    return render(request, 'TechShelterApp/cart.html',context)

def updateItem(request):

    user = request.user 
    orderinfo, created = OrderInfo.objects.get_or_create(customer=user, complete=False)
    
    data = json.loads(request.body)
    techId = data['techId']
    tech = Tech.objects.get(id=techId)
    
    orderedTech, created = OrderedTech.objects.get_or_create(order=orderinfo, tech=tech) 
    
    action = data['action']
    if action == 'add':
        orderedTech.quantity = (orderedTech.quantity + 1)
    elif action == 'remove':
        orderedTech.quantity = (orderedTech.quantity - 1)

    orderedTech.save()

    if orderedTech.quantity <= 0:
        orderedTech.delete()

    return JsonResponse('Item was added', safe=False)

import datetime

def checkout(request):
    
    if request.user.is_authenticated:
        logged_in_user = request.user 
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()
        form = DeliveryForm(request.POST, request.FILES)

        if request.method == 'POST':
            transaction_id = datetime.datetime.now().timestamp()
            orderinfo.transaction_id = transaction_id
            orderinfo.complete = True
            orderinfo.save()
        
            if orderinfo.shipping == True:
                if form.is_valid():
                    newDelivery = form.save(commit=False)
                    newDelivery.customer = request.user
                    newDelivery.order = orderinfo
                    newDelivery.save()
            techs = Tech.objects.all()
            orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
            orderedtechs = orderinfo.orderedtech_set.all()
            context = {'techs':techs, 'logged_in_user':logged_in_user, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
            return render(request, 'TechShelterApp/tech_shelter.html',context)
    else:
        logged_in_user = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []
        print('User is not logged in..')

    context = {'logged_in_user':logged_in_user, 'orderedtechs':orderedtechs,'orderinfo':orderinfo, 'form':form}
    return render(request, 'TechShelterApp/checkout.html',context)


def my_tech_shelter(request):

    if request.user.is_authenticated:
        logged_in_user = request.user        
        user = request.user 
    else:
        user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
    techs = Tech.objects.filter(seller=user)
    context = {'logged_in_user':logged_in_user, 'user':user, 'techs':techs}
    return render(request, 'TechShelterApp/tech_shelter_stall.html',context)

def user_tech_shelter(request, userID):
    if userID != "":
        user = User.objects.get(id=userID)  
        techs = Tech.objects.filter(seller=user)
    else:
        user = "Unknown"
        techs = []

    if request.user.is_authenticated:
        logged_in_user = request.user
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()       
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []
    
    context = {'logged_in_user':logged_in_user, 'user':user, 'techs':techs, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
    return render(request, 'TechShelterApp/tech_shelter_stall.html',context)


def manageTechs(request):


    if request.user.is_authenticated:
        logged_in_user = request.user
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()       
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []
    
    techs = Tech.objects.all()
    context = {'logged_in_user':logged_in_user, 'techs':techs, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
    return render(request, 'TechShelterApp/managetechs.html',context)

def manageMyTechs(request):

    if request.user.is_authenticated:
        logged_in_user = request.user        
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
    techs = Tech.objects.filter(seller=logged_in_user)
    context = {'logged_in_user':logged_in_user, 'techs':techs}
    return render(request, 'TechShelterApp/managetechs.html',context)

def addTech(request):

    form = TechForm()
    
    if request.user.is_authenticated:
        logged_in_user = request.user
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()       
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []

    if request.method == 'POST':
        form = TechForm(request.POST, request.FILES)     

        if form.is_valid():
            newTech = form.save(commit=False)
            newTech.seller = request.user
            form.save()
            
        if 'Seller' in logged_in_user.usertype:
            techs = Tech.objects.filter(seller=logged_in_user)
        elif logged_in_user.is_superuser or logged_in_user.is_staff:
            techs = Tech.objects.all()
        context = {'form':form, 'logged_in_user':logged_in_user, 'techs':techs, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
        return render(request, 'TechShelterApp/managetechs.html',context)


    techs = Tech.objects.all()
    context = {'form':form, 'logged_in_user':logged_in_user, 'techs':techs}

    return render(request, 'TechShelterApp/addtech.html',context)

def updateTech(request, techID):
    form = TechForm()
    this_tech = Tech.objects.get(id=techID)
    form = TechForm(instance=this_tech)

    if request.user.is_authenticated:
        logged_in_user = request.user
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()       
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []

    if request.method == 'POST':
        form = TechForm(request.POST, request.FILES, instance=this_tech)
        if form.is_valid():
            form.save()
        if 'Seller' in logged_in_user.usertype:
            techs = Tech.objects.filter(seller=logged_in_user)
        elif logged_in_user.is_superuser or logged_in_user.is_staff:
            techs = Tech.objects.all()
        context = {'form':form, 'logged_in_user':logged_in_user, 'techs':techs}
        return render(request, 'TechShelterApp/managetechs.html',context)
    
    if request.method == 'FILES':
        #to see what info are input, in console, uncomment the line below
        #print('Printing POST:', request.POST)
        form = TechForm(request.FILES, instance=this_tech)
        if form.is_valid():
            form.update()
            
    context = {'form':form, 'logged_in_user':logged_in_user, 'this_tech': this_tech, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
    return render(request, 'TechShelterApp/updatetech.html',context)


def deleteTech(request, techID):

    if request.user.is_authenticated:
        logged_in_user = request.user
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()       
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []

    try:
        this_tech = Tech.objects.get(id=techID)
    except Tech.DoesNotExist:
        raise Http404("Tech does not exist")

    if request.method == 'POST':
        this_tech.delete()
        if 'Seller' in logged_in_user.usertype:
            techs = Tech.objects.filter(seller=logged_in_user)
        elif logged_in_user.is_superuser or logged_in_user.is_staff:
            techs = Tech.objects.all()
        
        context = {'logged_in_user':logged_in_user, 'techs':techs, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
        return render(request, 'TechShelterApp/managetechs.html',context)
    
    context = {'this_tech': this_tech}
    return render(request, 'TechShelterApp/deletetech.html',context)

def signup(request):
    
    if request.user.is_authenticated:
        logged_in_user=request.user
    else:
        logged_in_user = {
			'name':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
		}

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sign up successful")
            techs = Tech.objects.all()  
            return render(request, 'TechShelterApp/tech_shelter.html', {'logged_in_user':logged_in_user, 'techs':techs})
        else:
            messages.error(request, "Please use valid Username and Password!")  
    
    form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})
    

def logout(request):
    logout(request)
    return HttpResponse('TechShelterApp/tech_shelter.html')

def users(request):
    if request.user.is_authenticated:
        logged_in_user = request.user
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()       
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []

    if request.user.is_superuser:
        users = User.objects.all()       
    else:
        users = {}
       
    context = {'logged_in_user':logged_in_user, 'users':users, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
    return render(request, 'TechShelterApp/users.html',context)



def editprofile(request, userID):
    if request.user.is_authenticated:
        logged_in_user = request.user
        orderinfo, created = OrderInfo.objects.get_or_create(customer=logged_in_user, complete=False)
        orderedtechs = orderinfo.orderedtech_set.all()       
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
        orderinfo = {'get_cart_total_price': 0, 'get_cart_item_quantity': 0, 'shipping': False}
        orderedtechs = []
    if request.user.is_superuser:
        form = Admin_UserUpdateForm()
        users = User.objects.all() 
        try:
            user = User.objects.get(id=userID)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        form = Admin_UserUpdateForm(instance=user)

        if request.method == 'POST':
            #to see what info are input, in console, uncomment the line below
            #print('Printing POST:', request.POST)
            form = Admin_UserUpdateForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                context = {'logged_in_user':logged_in_user, 'users':users}
                return render(request, 'TechShelterApp/users.html',context)
    
        if request.method == 'FILES':
            #to see what info are input, in console, uncomment the line below
            #print('Printing POST:', request.POST)
            form = Admin_UserUpdateForm(request.FILES, instance=user)
            if form.is_valid():
                form.update()
            
    else:
        form = UserUpdateForm()
        user = request.user
        users = {}
        form = UserUpdateForm(instance=user)

        if request.method == 'POST':
            #to see what info are input, in console, uncomment the line below
            #print('Printing POST:', request.POST)
            form = UserUpdateForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
    
        if request.method == 'FILES':
            #to see what info are input, in console, uncomment the line below
            #print('Printing POST:', request.POST)
            form = UserUpdateForm(request.FILES, instance=user)
            if form.is_valid():
                form.update()
    
    context = {'logged_in_user':logged_in_user, 'form':form, 'user':user, 'orderedtechs':orderedtechs,'orderinfo':orderinfo}
    return render(request, 'TechShelterApp/editprofile.html',context)

def deactivateprofile(request, userID):
    if request.user.is_authenticated:
        logged_in_user = request.user        
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }

    if request.user.is_superuser:
        try:
            user = User.objects.get(id=userID)
            if user.is_active==True:
                user.is_active = False
            messages.success(request, "The account is deactivated")
        except User.DoesNotExist:
            messages.error(request, "User does not exist")  
            return render(request, 'TechShelterApp/users.html')
        except Exception as e: 
            return render(request, 'TechShelterApp/users.html',{'err':e})
        
        users = User.objects.all()       
    else:
        users = {}
       
    context = {'logged_in_user':logged_in_user,'users':users}
    if request.user.is_superuser:
        return render(request, 'TechShelterApp/users.html',context)  
    else:
        return render(request, 'TechShelterApp/tech_shelter.html',context)  

def deleteprofile(request, userID):
    if request.user.is_authenticated:
        logged_in_user = request.user        
    else:
        logged_in_user = {
			'username':'guest',
			'imageURL':'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png',
			'email':'null'
        }
    if request.user.is_superuser:
        try:
            user = User.objects.get(id=userID)
            user.delete()
            messages.success(request, "The user is deleted")
        except User.DoesNotExist:
            messages.error(request, "User does not exist")  
            return render(request, 'TechShelterApp/users.html')
        except Exception as e: 
            return render(request, 'TechShelterApp/users.html',{'err':e})
        
        users = User.objects.all()       
    else:
        users = {}
       
    context = {'logged_in_user':logged_in_user, 'users':users}
    return render(request, 'TechShelterApp/users.html',context)         


           
        

 