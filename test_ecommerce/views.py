from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Product
from django.contrib import messages

# Create your views here.

def index(request):
    fea=Product.objects.filter(flag="F")
    sli=Product.objects.filter(flag="S")
    lat=Product.objects.filter(flag="L")
    return render(request,'index.html',{'fea':fea,'lat':lat,'sli':sli})
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if(User.objects.filter(username=username).exists()):
                messages.warning(request,"User Name Already Exists")
                return redirect('register')
            elif(User.objects.filter(email=email).exists()):
                messages.warning(request,"Email Already Exists")
                return redirect('register')
            else:
                user=User.objects.create_user(
                    password=password1,  
                    username=username, 
                    first_name=first_name, 
                    last_name=last_name, 
                    email=email,
                )
                user.save()
                messages.success(request,"User Created")
                return redirect('register')
        else:
            messages.warning(request,"User Password MisMatching")
            return redirect('register')

    else:
        return render(request,'checkout-shipping.html')
def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if request.method=="POST":
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/test_ecommerce/')
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,"checkout-shipping.html")
def logout(request):
    auth.logout(request)
    return redirect("/test_ecommerce/")

