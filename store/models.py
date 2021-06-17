from django.db import models

# Create your models here.
#use of pillow


class Category(models.Model):
    name = models.CharField(max_length=100)


    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_id(category_id):
        if category_id:

            return Product.objects.filter(category=category_id)

        else:
            return Product.get_all_products()

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def isExist(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False



