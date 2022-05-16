from django.contrib import admin
from cshopapi.models import  Registration,Category,Clothes,Checkout,Cart
# Register your models here.
admin.site.register(Registration)
admin.site.register(Category)
admin.site.register(Clothes)
admin.site.register(Checkout)
admin.site.register(Cart)