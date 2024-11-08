from django import forms

from .models import Product

# sample. research on this topic, 
# similar to serializers
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]
