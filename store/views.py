from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category

# Create your views here.

def index(request):
    categories=Category.get_all_categories()
    products = None
    # print(products)
    categoryID=request.GET.get('category')
    if categoryID:
        products = Product.get_products_by_id(categoryID)
    else:
        products = Product.get_all_products()
    data= {}
    data['products']=products
    data['categories']=categories
    
    return render(request,'index.html',data)