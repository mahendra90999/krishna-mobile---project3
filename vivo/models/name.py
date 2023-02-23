from django.db import models
from .product import Product


class Name(models.Model):
    co_name = models.ForeignKey(Product,on_delete=models.CASCADE)
    co_name1 = models.CharField(max_length=100,default="")
    stars = models.IntegerField()


    @staticmethod
    def get_all_name():
        return Name.objects.values('co_name1')

    