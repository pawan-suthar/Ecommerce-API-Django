from rest_framework import viewsets
from rest_framework.response import Response
from Ecom.product.models import (Product,Brand,Category)
from Ecom.product.serilizer import (ProductSer,categorySer,BrandSer)
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework.decorators import action


class CategoryViewSet(viewsets.ViewSet):
    """
    view set for category list

    """
    queryset = Category.objects.all()
    @action(detail=False,methods=['get'], url_path=r"(?P<category>\w+)/all")
    def list_product_by_category(self,request,category= None):
        pdbyct = ProductSer(Product.objects.all(category__name = category))
        return Response(pdbyct.data)
    
    # to Show table in API Doc Swagger
    serializer_class = categorySer
    @extend_schema(request = categorySer)
    def list(self, request):
        
        serializer = categorySer(self.queryset, many=True)
        return Response(serializer.data)
    

class ProductViewSet(viewsets.ViewSet):
    """
    view set for product list
    """
    queryset = Product.objects.all()

     # to Show table in API Doc Swagger
    serializer_class = ProductSer
    @extend_schema(request = ProductSer)
    def list(self, request):
    
        serializer = ProductSer(self.queryset, many=True)
        return Response(serializer.data)
    

    

class BrandViewSet(viewsets.ViewSet):
    """
    view set for Brand list
    """
     # to Show table in API Doc Swagger
    serializer_class = BrandSer
    @extend_schema(request = BrandSer)
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSer(queryset, many=True)
        return Response(serializer.data)

