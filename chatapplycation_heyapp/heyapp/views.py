from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Message
from django.contrib import messages
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
import random




def homefunc (request):
     return render(request,'home.html')

def reg(request):
     return render(request, 'signup.html')


def loginfunc (request):
     return render(request,'login.html')

def signup_OTPfunc (request):
     return render(request,'signup_OTP.html')

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

     if User.objects.filter(email=mail).exists():
          usercheck = User.objects.get(email=mail)
          if usercheck.password == pwd:
               return render(request, 'home.html')
          else:
               messages.success(request, "Password Incorrect")
               return render(request, 'login.html')
     else:
          messages.success(request, "Email is Not Registered")
          return render(request, 'login.html')




#add otp genarator and sendmail code

def otpgenarator():
     random_number = random.randrange(1000, 10000)
     return random_number


def sendemail(request):
     code = otpgenarator()
     request.session['otp_code'] = code

     if request.method == "POST":
          sender = 'hay app team'
          toemail = request.POST.get('email')
          toname = "New user"
          fromemail = "shankumarasinha6@gmail.com"
          subject = "your otp verification code"
          message = str(code)

          configuration = sib_api_v3_sdk.Configuration()
          configuration.api_key[
               'api-key'] = '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'
          api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
          subject = subject
          html_content = message
          sender = {"name": sender, "email": fromemail}
          to = [{"email": toemail, "name": toname}]
          headers = {"Some-Custom-Name": "unique-id-1234"}
          send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers, html_content=html_content,
                                                         sender=sender, subject=subject)
          try:
               api_response = api_instance.send_transac_email(send_smtp_email)
               pprint(api_response)
               messages.success(request, "otp code  send successfully")
          except ApiException as e:
               print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
     return render(request, 'signup_OTP.html', locals())


def verifyotp(request):
     if request.method == "POST":
          otp = request.POST.get('otp')
          otp_code = request.session.get('otp_code')
          otp = int(otp)
          if otp_code != otp:
               return redirect('signup_OTP')

     return render(request, 'home.html', locals())



def userlistfunc(request):
     
     users = User.objects.all()
     return render(request, 'userlist.html', {'users': users})

   
 

def messagelistfunc(request, receivername): 
    chat = Message.objects.filter( recever=receivername)
    return render(request, 'chat.html', {'chats': chat})


def sendmsg(request):
     msg=request.POST['message']
     msgsender="rashin"
     receiver="pramod"

     new_message=Message.objects.create( message=msg,sender=msgsender,recever=receiver)
     
     new_message.save()
     return HttpResponse('Message sent successfully')









