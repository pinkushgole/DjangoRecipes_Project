from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User=get_user_model()


# Create your views here.

@login_required(login_url="/login/")
def receipes(request):
    if request.method=="POST":
      data=request.POST
      receipe_image=request.FILES.get('receipe_image')
      receipe_name=data.get('receipe_name')
      receipe_description=data.get('receipe_description')
       
      Receipe.objects.create(receipe_name=receipe_name,
                             receipe_description=receipe_description,
                             receipe_image=receipe_image,
                             )
      return redirect('/receipes/')
    
    queryset=Receipe.objects.all()
    
    if request.GET.get('search'):
       print(request.GET.get('search'))
       queryset=queryset.filter(receipe_name__icontains = request.GET.get('search'))



    context={
       'receipes':queryset
    }

    return render(request,"receipe.html",context)

def delete_receipe(request,id):
   queryset=Receipe.objects.get(id=id)
   print(id)
   queryset.delete()
   return redirect('/receipes/')

def update_receipe(request,id):
   queryset=Receipe.objects.get(id=id)
   
   
   if request.method=="POST":
      data=request.POST

      receipe_image=request.FILES.get('receipe_image')
      receipe_name=data.get('receipe_name')
      receipe_description=data.get('receipe_description')
      
      queryset.receipe_name=receipe_name
      queryset.receipe_description=receipe_description

      if receipe_image:
        queryset.receipe_image=receipe_image
      
      queryset.save()

      return redirect('/receipes/')
   
   context={
       'receipe':queryset
    }

   return render(request,"update.html",context)
   
def register_page(request):
    
    if request.method=="POST":
       first_name=request.POST.get('first_name')
       last_name=request.POST.get('last_name')
       username=request.POST.get('username')
       password=request.POST.get('password')
       
       user=User.objects.filter(username=username)

       if user.exists():
          messages.info(request,'user name alredy exist')
          return redirect('/register/')

       user=User.objects.create(
          first_name=first_name,
          last_name=last_name,
          username=username,
       )
       user.set_password(password)

       user.save()
       messages.info(request,'!!!! Registertion successfully !!!!')
       return redirect('/register/')

    return render(request,"register.html")

def login_page(request):
    
    if request.method=="POST":
       username=request.POST.get("username")
       password=request.POST.get("password")
       print(username,password)

       if not User.objects.filter(username = username).exists():
         messages.info(request,'Invailid Username')
         return redirect('/login/')

       user=authenticate(username=username,password=password)

       if user is None:
           messages.info(request,'Invailid Password')
           return redirect('/login/')
       else:
         #  login session me user ko save kar deti hai ki session yaad rakhe 
          login(request,user)
          return redirect('/receipes/')


    return render(request,"login.html")


def user_logout(request):
    logout(request)
    messages.info(request,'User Logout !!!!! ')
    return redirect('/login/')
