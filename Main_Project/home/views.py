from django.shortcuts import render
from django.http import HttpResponse

def home1(request):
    pepoles=[
      {'name':'Sonu','age':19},
      {'name':'Raja','age':23},
      {'name':'Ajay','age':15},
      {'name':'Vijay','age':20},
    ]
    return render(request,"index.html",{"pepoles":pepoles,"title":"Home Page"})

def contact(request):
    context="Contact Page"
    return render(request,"contact.html",context)