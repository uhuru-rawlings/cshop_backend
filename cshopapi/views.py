from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
import jwt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from cshopapi.models import  Registration,Category,Clothes,Checkout,Cart
from cshopapi.serializers import RegistrationSerializers,CategorySerializer,ClothesSerializer,CheckoutSerializer,CartSerializer
# Create your views here.

@api_view(['POST'])
def register_user(request):
    details = request.data
    useremail = details['useremail']
    password = details['password']

    checkuser = Registration.objects.filter(useremail = useremail)
    if checkuser.exists():
        return Response({"error":"sorry this user already exist."})
    else:
        new_user = Registration(useremail = useremail,password = make_password(password))
        new_user.save()
        return Response({"success":"Registration successful."})