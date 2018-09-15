from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home_view(request, *args, **kargs):
    print(args, kargs)
    print(request.user)
    return render( request, "home.html", {} )

def contact_view(request, *args, **kargs):
    return render( request, "contact.html", {} )

def about_view(request, *args, **kargs):

    my_context = {
        "name" : "deepak",
        "number" : 1234, 
        "list" : [1, 2, 3, 4]
    }
    return render( request, "about.html", my_context )

def api(*args, **kargs):
    return JsonResponse({'status':"OK", 'response_code' : "200"})