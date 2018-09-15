from django.shortcuts import render

from .models import Product
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=2)
    context = {

        "title" : obj.title,
        "description" : obj.description,
        "price" : obj.price
    }
    return render(request, "product/details.html", context)