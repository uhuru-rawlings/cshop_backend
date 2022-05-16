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