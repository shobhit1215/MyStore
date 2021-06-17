from django.contrib import admin

# Register your models here.
from .models import Product,Category,Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','phone','email','password']


admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
