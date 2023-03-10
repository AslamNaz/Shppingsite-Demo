from django.shortcuts import render, redirect
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def cart_Details(request,tot=0,count=0,cart_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects,filter(cart=ct, active=True)
        for i in ct_items:
            tot+=(i.prodt.price*i.quan)
            count+=i.quan
    except ObjectDoesNotExist:
        pass
    return render(request,'Cart.html',{'ci':ct_items,'t':tot,'cn':count})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id


def add_cart(request, product_id):
    prodt=Products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prodt,cart=ct)
        if c_items.quan< c_items.prodt.stock:
            c_items.quan+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prodt,quan=1,cart=ct)
        c_items.save()
    return redirect('cardDetails/')

    pass

def min_cart(request):
    pass

def cart_delete(request):
    pass