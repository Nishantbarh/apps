from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


#/products--


def index(request):
    products = Product.objects.all()
    #return HttpResponse('hello World')
    return render(request,'index.html', {'products': products})


def newproduct(request):
    return HttpResponse('new product')


