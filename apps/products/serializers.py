from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.products.models import Product, ProductOption, ProductOptionItem, ProductVariant


class ProductOptionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionItem
        fields = ['item_name']


class ProductOptionSerializer(serializers.ModelSerializer):
    items = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = ProductOption
        fields = ['option_name', 'items']
        # validators = [
        #     UniqueValidator(
        #         queryset=ProductOption.objects.all(),
        #         message="A product option with this name already exists."
        #     )
        # ]


class ProductSerializer(serializers.ModelSerializer):
    options = ProductOptionSerializer(many=True)

    class Meta:
        model = Product
        fields = ['product_name', 'description', 'status', 'options']
