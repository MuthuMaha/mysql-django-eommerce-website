from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
        return render(request,"index.html",{"name":"Muthu"})
def addcal(request):
        return render(request,"add.html")
def result(request):
        num1=int(request.POST['first_number'])
        num2=int(request.POST['second_number'])
        res=num1+num2
        return render(request,"result.html",{"result":res})
