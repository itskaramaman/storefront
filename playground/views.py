from django.shortcuts import render
from store.models import Product


def say_hello(request):
    product_exists = Product.objects.filter(pk=0).exists()

    return render(request, 'hello.html', {'name': 'Mosh'})
