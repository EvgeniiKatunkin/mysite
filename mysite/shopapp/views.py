from django.http import HttpRequest
from django.shortcuts import render
from timeit import default_timer


def index(request: HttpRequest):
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Smartphone', 499),
    ]
    context = {
        'time_running': default_timer(),
        'products': products,
    }
    return render(request, 'shopapp/index.html', context=context)
