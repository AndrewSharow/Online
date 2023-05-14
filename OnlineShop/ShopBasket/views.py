from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.core.serializers import serialize

def set_cookie(request):
    response = render(request, 'basket.html')
    product_pk = request.GET.get("pk")
    if request.GET.get("method") == 'add':
        if "basket_items" in request.COOKIES:
            if product_pk not in request.COOKIES["basket_items"]:
                response.set_cookie("basket_items", request.COOKIES["basket_items"]+product_pk)
        else:
            response.set_cookie("basket_items", product_pk)
    if request.GET.get("method") == 'del':
        response = render(request, 'basket.html')
        cookie = request.COOKIES["basket_items"].replace(product_pk, '')
        if cookie == '':
            response.delete_cookie("basket_items")
        else:
            response.set_cookie("basket_items", cookie)
    return response

def show_shop(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products        
    return render(request, 'shop.html', context = context)


def show_basket(request):
    context = {}
    if "basket_items" in request.COOKIES:
        pk_list = list(request.COOKIES["basket_items"])
        products = []
        for pk in pk_list:
            product = Product.objects.get(pk = pk)
            products.append(product)
        context['products'] = products
    return render(request, 'basket.html', context)
