
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from cshopapi.views import register_user,login_user,decode_user,get_categories,get_clothes,checkout_view,cart_items,get_history

schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
    path("account/registration/",register_user),
    path("account/login/",login_user),
    path("account/user/",decode_user),
    path("cart/categories/",get_categories),
    path("cart/clothes/",get_clothes),
    path("cart/checkout/",checkout_view),
    path("cart/addcart/",cart_items),
    path("cart/getcart/<int:id>/",get_history),
]
