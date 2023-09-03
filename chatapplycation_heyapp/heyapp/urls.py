from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static   


urlpatterns = [

    path('sign_up/',views.reg,name='sign_up' ),
    path('home/',views.homefunc,name='home' ),
   
    path('login/',views.loginfunc,name='login' ),
    path('signup_OTP/',views.signup_OTPfunc,name='signup_OTP' ),
    path('userlistfunc/',views.userlistfunc,name='userlistfunc' ),
    path('register/',views.register,name='register' ),
    path('gohome/',views.gohome,name='gohome' ),
    path('sendemail/', views.sendemail, name="sendemail"),
    path('verifyotp/', views.verifyotp, name="verifyotp"),
    path('messagelistfunc/', views.messagelistfunc, name="messagelistfunc"),
    path('sendmsg/', views.sendmsg, name="sendmsg"),
    path('messagelistfunc/<str:receivername>/', views.messagelistfunc, name='messagelistfunc'),
]