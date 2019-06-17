from django.contrib import admin

# Register your models here.

from .models import Item, Cart, CartItem, Review, Login

admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Review)
admin.site.register(Login)
