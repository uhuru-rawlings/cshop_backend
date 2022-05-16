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

@api_view(['GET'])
def get_clothes(request):
    clothes =Clothes.objects.all()

    if clothes:
        serialize = ClothesSerializer(clothes, many = True)
        return Response(serialize.data)
    else:
        return Response([])

@api_view(['POST'])
def checkout_view(request):
    details = request.data
    user = details['user'] # should be id
    pickup_date = details['pickup_date']
    deliveryCity = details['deliveryCity']
    delivery_address = details['delivery_address']
    receiver_id = details['receiver_id']
    receiver_contact = details['receiver_contact']
    
    user = Registration.objects.get(id = user)
    new_checkout = Checkout(user = user,pickup_date = pickup_date,
                            deliveryCity = deliveryCity,
                            delivery_address = delivery_address,
                            receiver_id = receiver_id,
                            receiver_contact = receiver_contact)
    new_checkout.save()
    return Response({"success":"Check out successfull."})

@api_view(['POST'])
def cart_items(request):
    details = request.data 
    user = details["user"] #should be user id
    items = details["items"] #should be [{"id":1,"quantity":20}]
    quantity = details["quantity"]
    price = details["price"]
    date_added = details["date_added"]

    user = Registration.objects.get(id = user)
    for x in items:
        items = Clothes.objects.get(id = x.id)
        new_items = Cart(user = user,items = items,quantity = x.quantity,price = (x.quantity * items.item_price))
        new_items.save()

        return Response({"Successfully added to purchase history"})

@api_view(['GET'])
def get_history(request, id):
    user = Registration.objects.get(id = id)
    cart = Cart.objects.filter(user = user)
    if cart:
        serialize = CartSerializer(cart, many =True)
        return Response(serialize.data)
    else:
        return Response([])