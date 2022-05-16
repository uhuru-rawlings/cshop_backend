from django.db import models
from django.contrib.auth.hashers import make_password,check_password
import jwt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
# Create your models here.
