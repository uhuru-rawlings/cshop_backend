from pyexpat import model
from rest_framework.serializers import serializers
from cshopapi.models import  Registration,Category,Clothes,Checkout,Cart

class RegistrationSerializers(serializers.ModelsSerializer):
     class Meta:
         model = Registration
         fields = ["id","useremail"]

class CategorySerializer(serializers.Modelserializer):
    class Meta:
        model = Category
        fields = ["id","itemcategory"]

class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ["id","category","item_name","item_color","item_description","item_quantity","item_price","for_gender","date_added"]

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ["id","user","pickup_date","deliveryCity","delivery_address","receiver_id","receiver_contact","added_date"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        models = Cart
        fields = ["id","user","items","quantity","price","date_added"]