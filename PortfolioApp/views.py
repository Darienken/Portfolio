from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
# Create your views here.


def MainPage(request):
    
    if request.method=="POST":

        affair=request.POST["contact-me__input-affair"]
        name=request.POST["contact-me__input-name"]
        last_name=request.POST["contact-me__input-lastname"]
        message=request.POST["contact-me__input-message"]
        tel=request.POST["contact-me__input-tel"]
        mail=request.POST["contact-me__input-mail"]
        body=f"Name: {name} LastName: {last_name} Mail: {mail} Tel: {tel}/n{message}"
        
        send_mail(affair,body,settings.EMAIL_HOST_USER,["diegorpro2024@gmail.com"])

        return render(request, loader.get_template("MainPage.html"))

    
    return render(request, loader.get_template("MainPage.html"))