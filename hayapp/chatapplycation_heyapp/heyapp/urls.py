from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static   


urlpatterns = [


    path('',views.homefunc,name='home' ),
    path('home/',views.homefunc,name='home' ),
    path('chat/',views.chatfunc,name='chat' ),
    path('login/',views.loginfunc,name='login' ),
    path('signup_OTP/',views.signup_OTPfunc,name='signup_OTP' ),
    path('signup/',views.signupfunc,name='signup' ),
    path('userlist/',views.userlistfunc,name='userlist' ),
]