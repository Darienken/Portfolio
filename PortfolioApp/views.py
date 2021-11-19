from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
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

        return render(request, "C:/Users/Vivi/OneDrive/Escritorio/Didackmon_User001/thewise king hacka/Web Projects/Portfolio/PortfolioApp/templates/MainPage.html")

    
    return render(request,"C:/Users/Vivi/OneDrive/Escritorio/Didackmon_User001/thewise king hacka/Web Projects/Portfolio/PortfolioApp/templates/MainPage.html")