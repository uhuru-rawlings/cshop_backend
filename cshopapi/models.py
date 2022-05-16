from django.db import models

# Create your models here.

class Registration(models.Model):
    useremail = models.EmailField(max_length=300)
    password = models.CharField(max_length=366)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Registration'

    def __str__(self):
        return self.useremail
class Category(models.Model):
    itemcategory = models.CharField(max_length = 100)
    date_added = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.itemcategory

class Clothes(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    item_name = models.CharField(max_lenmgth = 100)
    item_color = models.CharField(max_lenmgth = 100)
    item_description = models.TextField(max_lenmgth = 100)
    item_quantity = models.IntegerField()
    item_price = models.IntegerField()
    for_gender = models.CharField(max_lenmgth = 100)
    date_added = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'Clothes'

    def __str__(self):
        return self.item_name

class Checkout(models.Model):
    user = models.ForeignKey(Registration, on_delete = models.CASCADE)
    pickup_date = models.DateField()
    deliveryCity = models.CharField(max_length = 100)
    delivery_address = models.CharField(max_length = 200)
    receiver_id = models.IntegerField()
    receiver_id = models.IntegerField()
    added_date = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'Checkout'

    def __str__(self):
        return self.deliveryCity

class Cart(models.Model):
    user = models.ForeignKey(Registration, on_delete = models.CASCADE)
    items = models.ForeignKey(Clothes, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'Cart'
    
    def __str__(self):
        return self.user.useremail