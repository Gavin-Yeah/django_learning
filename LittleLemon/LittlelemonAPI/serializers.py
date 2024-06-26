from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']
        

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.StringRelatedField()
    # category = CategorySerializer()
    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),
        view_name="category-detail"
    )
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock','price_after_tax','category']
        # depth = 1
    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)
        
        

class MenuItemSerializer2(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)
    

class MenuItemSerializer3(serializers.HyperlinkedModelSerializer):
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock','price_after_tax','category']
        # depth = 1
    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)
    
class MenuItemSerializer4(serializers.ModelSerializer):
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock','price_after_tax','category', 'category_id']
        # depth = 1
    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)