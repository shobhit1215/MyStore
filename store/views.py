from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Category,Customer
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$260000$13ogOr81RXXowrVUXv6SeC$xux9inZYGXShlFgK/uCWmh9rqJAVj4my7f0+fDqXc7g='))

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

def validate(customer):
    error_mssg=None
    fname=customer.first_name
    lname=customer.last_name
    
    if(not fname):
        error_mssg="First Name Required !!"
    elif len(fname)<2:
        error_mssg="First Name must be 2 character long"
    elif(not lname):
        error_mssg="Last Name Reguired"
    elif len(lname)<2:
        error_mssg="Last Name must be 2 character Long"
    elif(not customer.phone):
        error_mssg="Phone number required"
    elif len(customer.phone)<10:
        error_mssg="Phone Number must be 10 char Long"
    elif(not customer.email):
        error_mssg="Email Required"
    elif customer.email.find("@gmail.com")==-1:
        error_mssg="Not a Valid Email"
    elif len(customer.email)<11:
        error_mssg="Email must have 11 characters"
    elif(not customer.password):
        error_mssg="Password Required"
    elif len(customer.password)<5:
        error_mssg="Password must be 5 character long"
    elif customer.isExist():
        error_mssg = "Email already registered"
    return error_mssg


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
        error_mssg = validate(customer)

        if not error_mssg:
            customer.password=make_password(customer.password)
            customer.save()
            return redirect('homepage')
        else:
            data={
                'error':error_mssg,
                'values':value
            }
            return render(request,'signup.html',data)
        

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        email = request.POST.get('email')
        password=request.POST.get('password')
        try:
            customer = Customer.objects.get(email=email)
        except:
            customer = False
        error_mssg = None
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_mssg = "Wrong Password Entered"
        else:
            error_mssg = "Email is not registered"

        print(customer)
        return render(request,'login.html',{'error':error_mssg})