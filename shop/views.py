from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def products_list(request):
    products = Product.objects.all()
    return render(request, 'shop/products_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})





