from django.shortcuts import render
import re

from .models import User
from django.contrib.auth.hashers import BCryptPasswordHasher

from django.core.mail import send_mail
from django.conf import settings

def register(request):

    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        phone = request.POST['phone']
        password = request.POST['password']

        emailPattern = '.{2}\@[a-z]{5,}\.[a-z]{3}'
        phonePattern = '\d{11}'
        passwordPattern = '(?=.*[A-Z])(?=.*\d)(?=.*\W)'

        if not re.match(emailPattern, email):
            
            return render(request, "form.html", {"error": "enter valid email"})
        
        elif not re.match(passwordPattern, password) :
            return render(request, "form.html", {
                "error": "password must contain 1 alphabet, number and symbol"})
        elif not re.match(phonePattern, phone)  or len(phone) != 11:
            return render(request, "form.html", {
                "error": "must be 11 digit "})
        else:

            hashpwd = BCryptPasswordHasher(password) 

            new_user = User.objects.create(
                email = email,
                password = hashpwd,
                phone = phone,
                first_name = first_name
            )

            send_mail(
                subject=f"registration",
                message=f"http://localhost:8000/{new_user.id}/{new_user.email}",
                from_email= settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email]
            )


            return render(request, "form.html", {"success": "success"})


    return render(request, "form.html")

