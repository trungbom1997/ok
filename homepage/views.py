from django.shortcuts import render
from .models import Customer
from Product.models import Category,Product
import hashlib
from .forms import CustomerForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def getcate():
        return Product.objects.filter(status_pro=True)
def homepage(request):
        pro = getcate()
        key=''
        if 'keyword' in request.GET:
                try:
                        key = request.GET.get('keyword')
                        pro = Product.objects.filter(name_pro__contains = key,status_pro=True)
                except:
                        return render(request, 'homepage/index.html')
        paginator = Paginator(pro, 8)
        page = request.GET.get('page', 1)
        try:
                orders_paged = paginator.page(page)
        except PageNotAnInteger:
                orders_paged = paginator.page(1)
        except EmptyPage:
                orders_paged = paginator.page(paginator.num_pages)
        cate = Category.objects.filter(status_cate=True)
        load = {'cate':cate,'pro':orders_paged,'key':key}
        return render(request,'homepage/index.html',load)

def register(request):
        form = CustomerForm()
        mess=''
        if request.method == "POST" :
                form = CustomerForm(request.POST)
                if form.is_valid():
                        form.Save()
                        form = CustomerForm()
                        mess="thanh cong"
        return render(request, 'homepage/register.html', {'form':form,'mess':mess})
def login(request):
        if request.method == "POST" :
                try:
                        user = request.POST['user']
                        password = hashlib.md5(request.POST['password'].encode("utf-8")).hexdigest()
                        cus = Customer.objects.get(user=user,password=password)
                        request.session['userid']=cus.id
                        return HttpResponseRedirect('/')

                except:
                        pass
        return render(request, 'homepage/login.html')


def categoryView(request,key):
        procate = Product.objects.filter(category__name_cate=key.replace("-"," "),category__status_cate=True)
        paginator = Paginator(procate, 8)
        page = request.GET.get('page', 1)
        try:
                orders_paged = paginator.page(page)
        except PageNotAnInteger:
                orders_paged = paginator.page(1)
        except EmptyPage:
                orders_paged = paginator.page(paginator.num_pages)

        return render(request, 'homepage/category.html',{'procate':orders_paged})






