from django.shortcuts import render
from itertools import chain

# Create your views here.
import os
import bcrypt
import datetime
from django.shortcuts import render
from .models import Adminlogins
from .models import Surveyinfo
from .models import SurveyLogin
from django.db.models import Q

def Login(request):
    return render(request,'admin/Login.html')


def CheckAdminLogin(request):
    try:
        result = request.session['ADMIN']
        return render(request, "admin/Dashboard.html", {'result': result})
    except  Exception as e:
        pass
    try:
        emailid = request.POST['emailid']
        password = request.POST['password']
        admin=Adminlogins.objects.get(email=emailid, user_status=1)
        # Adminlogins.ob
        if bcrypt.checkpw(password.encode("utf8"), admin.password.encode("utf8")):
            result=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).count()
            if (result):
                request.session['ADMIN'] = result
            print((result))
            return render(request, "admin/Dashboard.html",{'result':result})
        else:
            return render(request, "admin/Login.html", { 'msg': 'Invalid Userid or Password'})

    except Exception as e:
          print(e)

          return render(request, "admin/Login.html", {'msg': 'Server Error'})
#

def Info(request):
    try:
        t=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact=""))
        todayregistered=t.filter(Q(created_at=datetime.date.today())).count()
        totalregistered=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).count()
        totalempverified = Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).filter(Q(profile_img_status=1) & Q(aadhar_front_uri_status=1) & Q(aadhar_back_uri_status=1) & Q(driving_licence_status=1) & Q(full_size_img_status=1) & Q(college_id_img_status=1) & Q(tenth_img_status=1) & Q(twelth_img_status=1) & Q(address_img_status=1) & Q(vaccination_img_status=1) & Q(police_verification_img_status=1) & Q(semester_img_status=1)).count()
        pendingempverified = Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).filter(~Q(profile_img_status=1) & ~Q(aadhar_front_uri_status=1) & ~Q(aadhar_back_uri_status=1) & ~Q(driving_licence_status=1) & ~Q(full_size_img_status=1) & ~Q(college_id_img_status=1) & ~Q(tenth_img_status=1) & ~Q(twelth_img_status=1) & ~Q(address_img_status=1) & ~Q(vaccination_img_status=1) & ~Q(police_verification_img_status=1) & ~Q(semester_img_status=1)).count()
        totalemponboard = Surveyinfo.objects.filter(~Q(order_id__exact='') | ~Q(voucher__exact='')).filter(survey_id__in=SurveyLogin.objects.filter(work_status=1)).count()
        pendingemponboard = Surveyinfo.objects.filter(~Q(order_id__exact='') | ~Q(voucher__exact='')).filter(survey_id__in=SurveyLogin.objects.filter(work_status=0)).count()

        return render(request,'admin/Info.html',{'pendingemponboard':pendingemponboard,'totalemponboard':totalemponboard,'pendingempverified':pendingempverified,'totalempverified':totalempverified,'todayregistered':todayregistered,'totalregisterd':totalregistered})
    except Exception as e:
        print("Error",e)
        return render(request,'admin/Info.html')
