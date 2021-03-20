from django.db import models

from django.contrib.auth.models import AbstractUser
from graphviz import Digraph
import pydotplus

# A seller or customer
class User(AbstractUser):
    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    
    CUSTOMER = 'Customer'
    SELLER = 'Seller'
    USER_TYPE_CHOICES = [(CUSTOMER, 'Customer'),(SELLER, 'Seller')]
    
    usertype = models.CharField(max_length=8,choices=USER_TYPE_CHOICES,default=CUSTOMER)
    
    def __str__(self):
    	return self.username
	
    # User profile picture
    @property
    def imageURL(self):
    	try:
    		url = self.image.url
    	except:
    		url = 'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png'
    	return url

class Tech(models.Model):
	seller = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True, blank=True)
	techname = models.CharField(max_length=200)
	price = models.FloatField()

    # True for digital, false for physical 
	digital = models.BooleanField(default=False,null=True, blank=True)
	picture = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.techname

	@property
	def pictureURL(self):
		try:
			url = self.picture.url
		except:
			url = 'static/media/placeholder.png'
		return url

#Each order given by a particular user(customer)
class OrderInfo(models.Model):
	customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping(self):#get if the item is digital or physical
		shipping = False
		orderedtechs = self.orderedtech_set.all() # reverse relation with OrderedTech (get all the OrderedTech objects belong to a single OrderInfo object)
		for orderedtech in orderedtechs:
			if orderedtech.tech.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total_price(self):#get price total for items in cart
		orderedtechs = self.orderedtech_set.all() # reverse relation with OrderedTech (get all the OrderedTech objects belong to a single OrderInfo object)
		cart_total_price=sum([orderedtech.get_total_price for orderedtech in orderedtechs])
		return cart_total_price

	@property
	def get_cart_item_quantity(self):#get number of items in cart
		orderedtechs = self.orderedtech_set.all() # reverse relation with OrderedTech (get all the OrderedTech objects belong to a single OrderInfo object)
		cart_item_quantity=sum([orderedtech.quantity for orderedtech in orderedtechs])
		return cart_item_quantity

#Each items in cart
class OrderedTech(models.Model):
	tech = models.ForeignKey(Tech, on_delete=models.CASCADE, null=True)
	order = models.ForeignKey(OrderInfo, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total_price(self):
		total_price=self.tech.price*self.quantity
		return total_price
	
class DeliveryLocation(models.Model):
	customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	order = models.ForeignKey(OrderInfo, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
