from rest_framework import serializers

from product.models import Product

class ProductInSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Product
        fields = ["libelle", "marque", "description"]