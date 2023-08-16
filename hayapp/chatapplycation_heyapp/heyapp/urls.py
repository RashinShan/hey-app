from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static   


urlpatterns = [


    path('',views.signup_OTPfunc,name='signup_OTP' ),
    path('home/',views.homefunc,name='home' ),
    path('chat/',views.chatfunc,name='chat' ),
    path('login/',views.loginfunc,name='login' ),
    path('signup_OTP/',views.signup_OTPfunc,name='signup_OTP' ),
    path('signup/',views.signupfunc,name='signup' ),
    path('userlist/',views.userlistfunc,name='userlist' ),
    path('sendemail/', views.sendemail, name="sendemail"),
    path('verifyotp/', views.verifyotp, name="verifyotp"),
]