"""In this Django REST Framework (DRF) code, a serializer named ProductSerializer is defined to convert Product model instances into JSON and validate JSON data to be saved as Product instances."""

from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    # the object is the model instance
    def get_my_discount(self, obj):
        return obj.get_discount()