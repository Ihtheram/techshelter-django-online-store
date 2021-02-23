from django.db import models

from django.contrib.auth.models import AbstractUser


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
	seller = models.ForeignKey(User, on_delete=models.SET_NULL, editable=False, null=True, blank=True)
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