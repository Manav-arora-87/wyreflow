from django.shortcuts import render

# Create your views here.
import os
import bcrypt
from django.shortcuts import render
from .models import Adminlogins
from .models import Surveyinfo
from django.db.models import Q

def Login(request):
    return render(request,'admin/Login.html')


def CheckAdminLogin(request):

    try:
        emailid = request.POST['emailid']
        password = request.POST['password']
        admin=Adminlogins.objects.get(email=emailid, user_status=1)
        # Adminlogins.ob
        if bcrypt.checkpw(password.encode("utf8"), admin.password.encode("utf8")):
            result=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).count()
            print((result))
            return render(request, "admin/Dashboard.html",{'result':result})
        else:
            return render(request, "admin/Login.html", { 'msg': 'Invalid Userid or Password'})

    except Exception as e:
          print(e)

          return render(request, "admin/Login.html", {'msg': 'Server Error'})

