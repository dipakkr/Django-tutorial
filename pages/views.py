from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home_view(request, *args, **kargs):
    print(args, kargs)
    print(request.user)
    return HttpResponse("<h1> This is home view page</h1>")

def contact_view(*args, **kargs):
    return HttpResponse("<h1> This is Contact view page</h1>")

def about_view(*args, **kargs):
    return HttpResponse("<h1> This is About view page</h1>")

def api(*args, **kargs):
    return JsonResponse({'status':"OK", 'response_code' : "200"})