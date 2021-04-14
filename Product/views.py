from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.template.loader import render_to_string

def detail(request,id):
        Pro = Product.objects.get(pk=id)
        return render(request, 'Product/prodetail.html', {'detail': Pro})

cart = {}
def addcart(request):
        if request.is_ajax():
                id= request.POST.get('id')
                num = request.POST.get('num')
                pro = Product.objects.get(pk=id)
                if id in cart.keys():
                        itemcart = {
                                'name':pro.name_pro,
                                'price':pro.price_pro,
                                'image':str(pro.image_pro),
                                'num':int(cart[id]['num']) + int(num)
                        }
                else:
                        itemcart = {
                                'name':pro.name_pro,
                                'price':pro.price_pro,
                                'image':str(pro.image_pro),
                                'num':num
                        }
        cart[id] = itemcart
        request.session['cart'] = cart
        return HttpResponse('ok')

def delecart(request):
        if request.is_ajax():
                id= request.POST.get('id')
                del cart[id]
                request.session['cart'] = cart
                cartinfo = request.session['cart']
                return render(request, 'Order/cart.html', {'cart': cartinfo})
def updatecart(request):
        cart = request.session['cart']
        if request.is_ajax():
                id= request.POST.get('id')
                num= request.POST.get('num')
                cart[id]['num'] = num
        request.session['cart'] = cart
        return HttpResponse('update ok')






