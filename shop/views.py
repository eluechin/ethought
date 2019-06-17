from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.forms import modelformset_factory, inlineformset_factory

from .models import Item, Cart, CartItem, Review, Login

# Create your views here.


def index(request):
    skey = request.session.session_key
    uname = request.session.get('uname', 'Guest')
    items = Item.objects.all()
    return render(request, 'shop/index.html', {'skey' : skey, 'items': items, 'uname' : uname})


def detail(request, item_id):
    skey = request.session.session_key
    uname = request.session.get('uname', 'Guest')
    item = Item.objects.get(pk=item_id)
    reviews = Review.objects.filter(item=item)
    return render(request, 'shop/detail.html', {'skey' : skey, 'item': item, 'reviews': reviews, 'uname' : uname})


def login(request):
    skey = request.session.session_key
    uname = request.session.get('uname', 'Guest')
    error = ""
    if request.method == "POST":
        username = request.POST.get('uname', False)
        password = request.POST.get('password', False)
        try:
            user = Login.objects.get(username=username, password=password)
            request.session["uname"] = user.username
            request.session.modified = True
            return redirect('/shop')
        except Login.DoesNotExist:
            error = "Login unsccessul. Try again."     
    return render(request, 'shop/login.html', {'skey' : skey, "error": error, 'uname' : uname})

def logout(request):
    try:
        del request.session['uname']
    except KeyError:
        pass
    return redirect('/shop')


def cart(request, cart_id):
    skey = request.session.session_key
    uname = request.session.get('uname', 'Guest')
    cart = Cart.objects.get(pk=cart_id)
    cartItem_List = CartItem.objects.filter(cart=cart)
    total = 0
    for i in cartItem_List:
        cartItem = CartItem.objects.get(pk=i.id)
        total += cartItem.quantity * cartItem.item.item_price
    return render(request, 'shop/cart.html', {'skey' : skey, 'cartitem_list': cartItem_List, 'total': total, 'uname' : uname})


def add_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    cart = Cart.objects.get(pk=1)
    cartItem = CartItem.objects.create(cart=cart, item=item, quantity=1)
    cartItem.save()
    return redirect('/shop')


def remove_from_cart(request, item_id):
    cartItem = CartItem.objects.get(pk=item_id).delete()
    return redirect('/shop')


def review(request, item_id):
    skey = request.session.session_key
    uname = request.session.get('uname', 'Guest')
    item = Item.objects.get(pk=item_id)
    if request.method == "POST":
        rating = request.POST.get('rating', False)
        review = request.POST.get('review', False)
        newReview = Review.objects.create(
            item=item, rating=rating, review=review)
        newReview.save()
        return redirect('/shop')
    return render(request, 'shop/review.html', {'skey' : skey, 'item': item, 'uname' : uname})
