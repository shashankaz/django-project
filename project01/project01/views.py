from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Django! This is the home page.")
    return render(request, "index.html")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")