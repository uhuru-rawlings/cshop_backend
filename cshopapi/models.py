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

class Category(models.Model):
    itemcategory = models.CharField(max_length = 100)
    date_added = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.itemcategory