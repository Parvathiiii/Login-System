from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from accounts.serializers import LoginDetailsSerializer
from accounts.models import LoginDetails

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            if LoginDetails.objects.filter(Username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif LoginDetails.objects.filter(Email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = LoginDetails(Username=username, Password=password, Email=email, FirstName=first_name, LastName=last_name)
                user.save()
 
                return redirect('login_user')
    else:
        return render(request, 'accounts/registration.html')
    
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=LoginDetails.objects.filter(Username=username, Password=password)

        if user is not None:
            return redirect('logged')
        else:
            messages.info(request,'Invalid Usernam or Password')
            return redirect('login_user')
    
    else:
        return render(request, 'accounts/login.html')
    
def home(request):
    return render(request, "accounts/home.html")

def logged(request):
    return render(request, "accounts/logged.html")

def logout_user(request):
    auth.logout(request)
    return redirect('home')


@api_view(['GET'])
def getData(request):
    data=LoginDetails.objects.all()
    serializer = LoginDetailsSerializer(data, many=True)
    return Response(serializer.data)

