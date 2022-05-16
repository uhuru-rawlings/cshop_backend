from lib2to3.pgen2 import token
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
import jwt,datetime
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

@api_view(['POST'])
def login_user(request):
    details = request.data
    useremail = details['useremail']
    password = details['password']

    checkuser = Registration.objects.filter(useremail = useremail)
    if checkuser.exists():
        checkuser = Registration.objects.get(useremail = useremail)
        if check_password(password, checkuser.password):
            payload= {
                "id":checkuser.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload,'secret',algorithm='SH256').decode='utf-8'

            return Response({"jwt":token})
        else:
            return Response({"error":"Wrong password, try again."})
    else:
        return Response({"error":"sorry this user do not exist."})

@api_view(['POST'])
def decode_user(request):
    details = request.data
    token = details['jtw']

    if token:
        try:
            user = jwt.decode(token,'secret',algorithm=['SH256'])
            serialize = RegistrationSerializers(user)
            return Response(serialize.data)
        except:
            return Response({"error":"user un Authenticated"})
    else:
        return Response({"error":"user un Authenticated"})


@api_view(['GET'])
def get_categories(request):
    categories =Category.objects.all()

    if categories:
        serialize = CategorySerializer(categories, many = True)
        return Response(serialize.data)
    else:
        return Response([])