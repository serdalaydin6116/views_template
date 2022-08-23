from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     html ="<h1>This is entrance to view lecture</h1>"
#     return HttpResponse(html)

def home(request):
    print(request)
    print(request.method)
    print(request.COOKIES)
    print(request.path)
    print(request.user)
    print(request.META)
   
    html ="<h1>This is entrance to view lecture</h1>"
    return HttpResponse(html)