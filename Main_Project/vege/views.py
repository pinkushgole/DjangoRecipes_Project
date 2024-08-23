from django.shortcuts import render,redirect
from .models import Receipe
# Create your views here.

def vege_home(request):
    if request.method=="POST":
      data=request.POST
      receipe_image=request.FILES.get('receipe_image')
      receipe_name=data.get('receipe_name')
      receipe_description=data.get('receipe_description')
       
      Receipe.objects.create(receipe_name=receipe_name,
                             receipe_description=receipe_description,
                             receipe_image=receipe_image,
                             )
      return redirect('/recipe/')
    queryset=Receipe.objects.all()
    print(type(queryset))
    context={
       'receipes':queryset
    }

    return render(request,"receipe.html",context)
