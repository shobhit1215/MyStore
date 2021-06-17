from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    products = Product.gel_all_products()
    # print(products)
    
    return render(request,'index.html',{'products':products})