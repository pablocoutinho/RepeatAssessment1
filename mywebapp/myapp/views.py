from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    # Retrieve a single product from the database based on its primary key (pk)
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# Add more views for create, update, and delete operations
