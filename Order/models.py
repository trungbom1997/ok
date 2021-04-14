from django.db import models
from homepage.models import Customer
from Product.models import Product

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
	address_ship = models.CharField(max_length=200)
	phone_ship = models.CharField(max_length=200)
	status_ship = models.BooleanField(default=True)
	date_added_ship = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.address_ship

class Order(models.Model):
	shippingaddress = models.ForeignKey(ShippingAddress,on_delete=models.SET_NULL,blank=True,null=True)
	date_orderd_order = models.DateTimeField(auto_now_add=True)
	status_order = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=200)
	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
	order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
	price_orderitem = models.IntegerField(default=0)
	quantity_orderitem = models.IntegerField(default=0)
	date_added_orderitem = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.order




