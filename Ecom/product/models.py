from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    category = TreeForeignKey('Category', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class productDetail(models.Model):
    price  = models.DecimalField(decimal_places=2,max_digits=5)
    stock = models.IntegerField()
    sku = models.CharField(max_length=255)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.price

