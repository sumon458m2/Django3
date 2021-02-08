from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
def authentication(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('employee,profile')
        else:
            messages.error(request,'Email or Password Invalid!')
    return render(request,"authentication/login.html")
def forgot_password(request):
    return render(request,"authentication/forgot.html")

def registration(request):
    if request.method=='POST':
        username=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm_password"]
        if password==confirm_password:
            if User.objects.filter(username=username).exits():
                messages.error(request,"username already exits")

            elif User.objects.filter(email=email).exits():
                messages.error(request,"Email Already exits")

            else:                              
                user=user.objects.create_user(username=username,password=password,email=email)
                user.save()
                return redirect("employee,profile")
        else:
            messages.error(request,"Password and confirm_password already Exits")
                             
    return render(request,'authentication/registration.html')
def userlogout(request):
    logout(request)
    messages.success(request,'Succssfully Logout!')
    return redirect('/authentication')
