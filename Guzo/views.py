from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    
    #dest1=Destination()
    #dest1.name='Addis Ababa'
    #dest1.price=900
    #dest1.offer=True
    
   

    dest=Destination.objects.all()
    return render(request,'index.html',{'destt':dest})
 
def destinations(request):
    dest=Destination.objects.all()
    return render(request,"destinations.html",{'dest':dest})