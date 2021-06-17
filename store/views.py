from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Category,Customer

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

def signup(request):
    if request.method == 'GET':

        return render(request,'signup.html')
    else:
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        phone=request.POST.get('phonenumber')
        email=request.POST.get('email')
        password=request.POST.get('password')
        #validation
        value={
            'fname':fname,
            'lname':lname,
            'phone':phone,
            'email':email
        }
        error_mssg=None
        customer = Customer(first_name=fname,last_name=lname,phone=phone,email=email,password=password)
        if(not fname):
            error_mssg="First Name Required !!"
        elif len(fname)<2:
            error_mssg="First Name must be 2 character long"
        elif(not lname):
            error_mssg="Last Name Reguired"
        elif len(lname)<2:
            error_mssg="Last Name must be 2 character Long"
        elif(not phone):
            error_mssg="Phone number required"
        elif len(phone)<10:
            error_mssg="Phone Number must be 10 char Long"
        elif(not email):
            error_mssg="Email Required"
        elif email.find("@gmail.com")==-1:
            error_mssg="Not a Valid Email"
        elif len(email)<11:
            error_mssg="Email must have 11 characters"
        elif(not password):
            error_mssg="Password Required"
        elif len(password)<5:
            error_mssg="Password must be 5 character long"
        elif customer.isExist():
            error_mssg = "Email already registered"

        if not error_mssg:
            customer.save()
            return redirect('homepage')
        else:
            data={
                'error':error_mssg,
                'values':value
            }
            return render(request,'signup.html',data)
        