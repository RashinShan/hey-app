from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Message


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



     new_user = User.objects.create(firstname=firstname, lastname=lastname, dob=dob, email=email, username=username, password=password)
     new_user.save()
     return HttpResponse('Data enter Successfully')

