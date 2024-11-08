"""In this Django REST Framework (DRF) code, a serializer named ProductSerializer is defined to convert Product model instances into JSON and validate JSON data to be saved as Product instances."""

from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # add custom field
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
        #  can rename
        # obj.user -> user.username
        # obj.category -> category


        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None

        return obj.get_discount()
    

# serializers are better than doing this, serializers can also validate fields 
"""     if model_data:
            data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price', 'sale_price'])"""

# can have multiple serializers for one model e.g.
# class PrimaryProductSerializer(serializers.ModelSerializer):
# class SecondaryProductSerializer(serializers.ModelSerializer):
# class TertiaryProductSerializer(serializers.ModelSerializer):