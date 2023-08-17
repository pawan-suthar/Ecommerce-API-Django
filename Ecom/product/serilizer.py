from rest_framework import serializers
from Ecom.product.models import Product,Brand,Category,productDetail


class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BrandSer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class categorySer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductDetailSer(serializers.ModelSerializer):
    class Meta:
        model = productDetail
        fields = '__all__'