from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
import jwt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from cshopapi.models import  Registration,Category,Clothes,Checkout,Cart
# Create your views here.
