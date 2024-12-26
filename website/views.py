from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is Index")

def about(request):
    return HttpResponse("This is about")

def contact(request):
    return HttpResponse("This is contact")

def services(request):
    return HttpResponse("This is service")

def properties(reqquest):
    return HttpResponse("This is properties")

def propertiesSingle(request):
    return HttpResponse("This is properties Single")

def blog(request):
    return HttpResponse("This is blog") 

def blogSingle(request):
    return HttpResponse("This is blog single")