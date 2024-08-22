from django.shortcuts import render
from django.http import HttpResponse

def home1(request):
    return render(request,"index.html")

def success_page(request):
    return HttpResponse("THis is success page")