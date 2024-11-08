# from django.shortcuts import render

# # Create your views here.

from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # override default create method
    def perform_create(self, serializer):
        # serializer.save(user=self=self.request.user)
        print('serialize data: ', serializer.validated_data)
        title = serializer.validate_data.get('title')
        content = serializer.validate_data.get('content') or None
        # or
        # content = serializer.validate_data.get('content') or title\
        # in js its equivalent to || e.g. content = getContent || title
        
        if content is None:
            content = title

        serializer.save(content)

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # Product.objects.get(pk='1')

product_detail_view = ProductDetailAPIView.as_view()