from django.shortcuts import render, get_object_or_404

from .forms import ProductForm

from .models import Product
# Create your views here.

def product_create_view(request):
    
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form' : form
    }

    return render(request, "product/product_create.html", context)

def product_detail_view(request):
    
    obj = get_object_or_404(Product)
    context = {

        "title" : obj.title,
        "description" : obj.description,
        "price" : obj.price
    }
    return render(request, "product/details.html", context)

def dynamic_lookup_view(request, id):

    obj = get_object_or_404(Product, id=id)
    context = {
        "title" : obj.title
    }

    return render(request, "product/details.html", context)