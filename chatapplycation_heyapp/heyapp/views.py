from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Message
from django.contrib import messages


def chatfunc (request):
    return render(request,'chat.html')

def homefunc (request):
     return render(request,'home.html')

def reg(request):
     return render(request, 'signup.html')


def loginfunc (request):
     return render(request,'login.html')

def signup_OTPfunc (request):
     return render(request,'signup_OTP.html')

def userlistfunc (request):
     return render(request,'userlist.html')

def register(request):
     firstname = request.POST['firstname']
     lastname = request.POST['lastname']
     dob = request.POST['dob']
     email = request.POST['email']
     username = request.POST['uname']
     password = request.POST['password']
     repass = request.POST['reenterpassword']


     if User.objects.filter(email=email).exists():
          messages.success(request, "Email is already registered.")
     else:
          if password != repass:
               messages.success(request, "Password is Not matching")
          else:
               new_user = User.objects.create(firstname=firstname, lastname=lastname, dob=dob, email=email, username=username, password=password)
               new_user.save()
               return render(request,'login.html')
     return render(request, 'signup.html')

def gohome(request):
     mail = request.POST['email_log']
     pwd = request.POST['password_log']

     usercheck = User.objects.get(email=mail)
     if usercheck.password == pwd:
          return render(request, 'home.html')
     else:
          messages.success(request, "Username or Password Incorrect")
          return render(request, 'login.html')




















