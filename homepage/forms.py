from django import forms
from .models import Customer
import hashlib

class CustomerForm(forms.Form):
	user = forms.CharField(label='user',max_length=100)
	username = forms.CharField(label='username',max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='password',max_length=100)
	email = forms.EmailField(label='email',max_length=100)
	phone = forms.CharField(label='phone',max_length=100)

	def clean_user(self):
		user = self.cleaned_data['user']
		try:
			Customer.objects.get(user=user)
		except:
			return user
		raise forms.ValidationError('tai khoan da ton tai')
	def Save(self):
		user = self.cleaned_data['user']
		username = self.cleaned_data['username']
		password = hashlib.md5(self.cleaned_data['password'].encode("utf-8")).hexdigest()
		email = self.cleaned_data['email']
		phone = self.cleaned_data['phone']
		a=Customer.objects.create(user=user,username=username,password=password,email=email,phone=phone)
		a.save()

