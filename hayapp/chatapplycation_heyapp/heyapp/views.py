from django.shortcuts import render
from django.http import HttpResponse


def chatfunc (request):
    return render(request,'chat.html')

def homefunc (request):
     return render(request,'home.html')

def loginfunc (request):
     return render(request,'login.html')

def signup_OTPfunc (request):
     return render(request,'signup_OTP.html')


def signupfunc (request):
     return render(request,'signup.html')

def userlistfunc (request):
     return render(request,'userlist.html')
