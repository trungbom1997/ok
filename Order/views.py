from django.shortcuts import render
from django.http import HttpResponse
from .models import ShippingAddress,Order,OrderItem
import datetime
import uuid



def viewcart(request):
      total=0
      if 'cart' in request.session:
            cart = request.session['cart']
            for key,value in cart.items():
                  total += int(value['price']) * int(value['num'])
      return render(request, 'Order/cart.html',{'total':total})

def checkout(request):
      address=''
      ad=''
      customerid = request.session['userid']
      total = 0

      try:
            address = ShippingAddress.objects.filter(customer=customerid)
            ad = ShippingAddress.objects.filter(customer=customerid).order_by('-date_added_ship').first()
      except:
            pass

      if 'cart' in request.session:
            cart = request.session['cart']
            for key, value in cart.items():
                  total += int(value['price']) * int(value['num'])

      form = {'addship': address,'vcl':ad,'total':total}
      return render(request, 'Order/checkout.html',form)

def updateaddress(request):
      if request.is_ajax():
            id = request.POST.get('id')
            now = datetime.datetime.now()
            ShippingAddress.objects.filter(pk=id).update(date_added_ship=now)
      return HttpResponse('update ok')

def addship(request):
      if request.is_ajax():
            customerid = request.session['userid']
            add = request.POST['add']
            phone = request.POST['phone']
            now = datetime.datetime.now()
            cus = ShippingAddress.objects.create(address_ship=add, phone_ship=phone, customer_id=customerid,status_ship=True,date_added_ship=now)
            cus.save()
      return HttpResponse('update ok')

def payment(request):
      id = uuid.uuid1()
      if 'submit' in request.POST:
            shippingid = request.POST['idshipping']
            transaction = id.int
            ord = Order(status_order=False,transaction_id=transaction,shippingaddress_id=shippingid)
            ord.save()

            cart = request.session['cart']
            for key, value in cart.items():
                  orderdetail = OrderItem(quantity_orderitem=value['num'],order_id=ord.id,product_id=key,price_orderitem=value['price'])
                  orderdetail.save()
                  cart={}
                  request.session['cart'] = cart

      return render(request, 'Order/checkout.html',)

def myaccount(request):
      customerid = request.session['userid']
      order = Order.objects.filter(shippingaddress__customer_id = customerid)
      return render(request, 'Order/Myaccount.html',{'list':order} )





