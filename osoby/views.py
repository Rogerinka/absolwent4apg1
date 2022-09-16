from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def index(request):
    return HttpResponse(":33")

def info(request):
    return HttpResponse("hihi")



