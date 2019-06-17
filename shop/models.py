from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_description_short = models.CharField(max_length=255, null=True)
    item_description = models.CharField(max_length=10000, null=True)
    item_price = models.DecimalField(max_digits=19,decimal_places=2)

class Cart(models.Model):
    cart_id = models.CharField(max_length=255)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)

class Login(models.Model):
    username = models.CharField(max_length=100)
    password =  models.CharField(max_length=100)

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)
    review = models.CharField(max_length=10000, null=True)