from django.db import models
from django.urls import reverse

class Category(models.Model):
	name_cate = models.CharField(max_length=100,default='')
	des_cate = models.TextField(default='')
	status_cate = models.BooleanField(default=True)
	catedetail = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
	def __str__(self):
		return "%s, --%s" %(self.catedetail, self.name_cate)
	def get_absolute_url(self):
		return reverse('homepage')

class Product(models.Model):
	name_pro = models.CharField(max_length=200, default='')
	category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
	price_pro = models.FloatField()
	des_pro = models.TextField(default='')
	image_pro = models.ImageField(upload_to='images/')
	status_pro = models.BooleanField(default=True)
	def __str__(self):
		return self.name_pro
