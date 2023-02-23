from django.db import models

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    comp_name = models.CharField(max_length=50,default="")
    series = models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=300)
    price=models.IntegerField(default=0)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="shop/images",default="")
   

    def __str__(self):
        return self.product_name


    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_name():
        return Product.objects.values('comp_name')

    @staticmethod
    def get_all_products_comp_name(comp_name):
        if comp_name:
            return Product.objects.filter(name=comp_name)
        else:
            return Product.get_all_products()
