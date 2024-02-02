from rest_framework import serializers
from .models  import*

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
