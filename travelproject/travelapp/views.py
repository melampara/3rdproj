from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request, "index.html",{'result':obj,'res':obj1})
    #name="india"
    #return render(request, "home.html",{"obj":name})
#def index(request):
    #return render(request,"home.html")
#def about(request):
    #return render(request,"about.html")
#def contact(request):
    #return HttpResponse("hello i am contact")
#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #z=x+y
    #s=x-y
    #d=x//y
    #m=x*y
    #return render(request,"result.html",{'additionresult':z,'multiplycationresult':m,'divisionresult':d,'subtractionresult':s})



