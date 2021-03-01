from django.contrib import admin
from django.urls import path,include
from Cyber import views

urlpatterns = [
    path('Home.html', views.Index, name='index'),
    path('Recomendation.html',views.Recomend,name = 'rec'),
    path('ChatWithUs.html',views.chat,name = 'chat'),
    path('Signin.html',views.sign,name = 'sign'),
    path('Greetings.html',views.gr, name = 'gr'),
    path('login.html',views.login, name = 'login'),
    path('lr.html',views.Lr,name = 'lr'),
    path('Email-Sender.html',views.Email_Sender,name = 'es'),
    path('WeatherE.html',views.WeatherEngine,name = 'WE'),
    path('Weather_Res.html',views.WeatherE,name = 'WR'),
    path('EmailRes.html',views.Email_Res,name = 'Res'),
]
