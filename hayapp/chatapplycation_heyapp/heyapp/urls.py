from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static   


urlpatterns = [


    path('',views.reg,name='sign_up' ),
    path('home/',views.homefunc,name='home' ),
    path('chat/',views.chatfunc,name='chat' ),
    path('login/',views.loginfunc,name='login' ),
    path('signup_OTP/',views.signup_OTPfunc,name='signup_OTP' ),
    path('userlist/',views.userlistfunc,name='userlist' ),
    path('register/',views.register,name='register' ),
]