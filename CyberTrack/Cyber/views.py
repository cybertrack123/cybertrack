from django.shortcuts import render,HttpResponse
from Cyber.models import Username,Commment
import smtplib
import geopy
import requests
import json,datetime
import webbrowser

# Create your views here.
def Index(request):
    return render(request,'Home.html')

def Recomend(request):
    Objects = Username.objects.all()   
    for i in Objects:
        d1 = {'UserName':i.User}
    return render(request,'Recomendation.html',d1)

def chat(request):
    return render(request, 'ChatWithUs.html')

def sign(request):
    Objects = Username.objects.all()
    for i in Objects:
        if i in Objects:
            return HttpResponse("<h1>You Should Not Have More Than One Account</h1>")
    return render(request, 'Signin.html')

def gr(request):
    name = request.POST.get('User Name')
    gmail = request.POST.get('Email')
    passw = request.POST.get('Pass')
    UserN = Username(User = name, Email= gmail, Pass=passw)
    UserN.save()
    d1 = {'m':name}
    return render(request,'Greetings.html',d1)

def login(request):
    return render(request, 'login.html')

def Email_Sender(request):
    return render(request, 'Email-Sender.html')

def Email_Res(request):
    Ema_name = request.GET.get('email_name')
    Ema = request.GET.get('email_sender')
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(Username.Email,Username.Pass)
    server.sendmail(Username.Email,Ema_name,Ema)
    return render(request,'EmailRes.html')

def Lr(request):
    p = request.POST.get('P')
    u = request.POST.get('User')
    k = Username.objects.all()
    for i in k:
        if i.User == u and i.Pass == p:
            return render(request, 'ChatWithUs.html')

        else:
            return render(request, 'Lr.html')

def WeatherEngine(request):
    return render(request, 'WeatherE.html')

def WeatherE(request):
    We = request.GET.get('WE')
    Timezone=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={We}&appid=8f347c63869080fb6f6b782c927be200")
    Weather = Timezone.text
    x = Timezone.json()
    y = x["main"]
    humidity = y["humidity"]
    pressure = y["pressure"]
    max_ = y["temp_max"]
    min_ = y["temp_min"]
    m = x["weather"]
    n = x["wind"]
    d1 = {'timezone':int(y["temp"]-272.15),'pressure':pressure,'humidity':humidity,'City_Name':We,'desc':m[0] ['description'],'min':int(min_-272),'max':int(max_)-272,'wind':n["speed"]}
    print(Weather)
    return render(request, 'Weather_Res.html',d1)

def AC(request):
    return render(request, 'AddComment.html')

def Com(request):
    Comment_text = request.GET.get('comments')
    Comment_Save = Commment(Comment_Text= Comment_text)
    Comment_Save.save()
    AddComment = Commment.objects.all()
    for items in AddComment:
        d2 = {'Comments':items}
    return render(request, 'Comment.html',d2)

