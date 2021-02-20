from django.db import models

from django.contrib.auth.models import AbstractUser

# A seller or customer
class User(AbstractUser):
    image = models.ImageField(null=True, blank=True)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    joindate = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=30, blank=True)
    
    CUSTOMER = 'Customer'
    SELLER = 'Seller'
    USER_TYPE_CHOICES = [(CUSTOMER, 'Customer'),(SELLER, 'Seller')]
    usertype = models.CharField(max_length=8,choices=USER_TYPE_CHOICES,default=CUSTOMER)

    def __str__(self):
    	return self.name
	
    # User profile picture
    @property
    def imageURL(self):
    	try:
    		url = self.image.url
    	except:
    		url = 'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png'
    	return url
