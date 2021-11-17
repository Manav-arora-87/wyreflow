from django.shortcuts import render

# Create your views here.
import os
import bcrypt
from django.shortcuts import render
from .models import Adminlogins


def Login(request):
    return render(request,'Login.html')


def CheckAdminLogin(request):

    try:
        emailid = request.POST['emailid']
        password = request.POST['password']
        admin=Adminlogins.objects.get(email=emailid, user_status=1)
        # Adminlogins.ob
        if bcrypt.checkpw(password.encode("utf8"), admin.password.encode("utf8")):
            return render(request, "Dashboard.html",)
        else:
            return render(request, "Login.html", { 'msg': 'Invalid Userid or Password'})

    except Exception as e:
          print(e)

          return render(request, "Login.html", {'msg': 'Server Error'})

