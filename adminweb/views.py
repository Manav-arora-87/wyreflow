import json
from django.shortcuts import redirect
from django.http import JsonResponse
# Create your views here.
import os
import bcrypt
import datetime
from django.shortcuts import render
from .models import Adminlogins
from .models import Surveyinfo
from .models import SurveyLogin
from .models import College
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
            request.session['ADMIN']=admin.id
            return redirect('admin-dashboard')
        else:
            return render(request, "admin/Login.html", { 'msg': 'Invalid Userid or Password'})

    except Exception as e:
          print(e)

          return render(request, "admin/Login.html", {'msg': 'Server Error'})

def Admindashboard(request):
    try:
        result = request.session['ADMIN']
        res = Surveyinfo.objects.filter(~Q(order_id__exact="") | ~Q(voucher__exact="")).count()

        return render(request, "admin/Dashboard.html", {'result': res})
    except  Exception as e:
        return redirect('admin-login')


def HiringInfo(request):
    try:
        result = request.session['ADMIN']
        t=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact=""))
        todayregistered=t.filter(Q(created_at=datetime.date.today())).count()
        totalregistered=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).count()
        totalempverified = Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).filter(Q(profile_img_status=1) & Q(aadhar_front_uri_status=1) & Q(aadhar_back_uri_status=1) & Q(driving_licence_status=1) & Q(full_size_img_status=1) & Q(college_id_img_status=1) & Q(tenth_img_status=1) & Q(twelth_img_status=1) & Q(address_img_status=1) & Q(vaccination_img_status=1) & Q(police_verification_img_status=1) & Q(semester_img_status=1)).count()
        pendingempverified = Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).filter(~Q(profile_img_status=1) & ~Q(aadhar_front_uri_status=1) & ~Q(aadhar_back_uri_status=1) & ~Q(driving_licence_status=1) & ~Q(full_size_img_status=1) & ~Q(college_id_img_status=1) & ~Q(tenth_img_status=1) & ~Q(twelth_img_status=1) & ~Q(address_img_status=1) & ~Q(vaccination_img_status=1) & ~Q(police_verification_img_status=1) & ~Q(semester_img_status=1)).count()
        totalemponboard = Surveyinfo.objects.filter(~Q(order_id__exact='') | ~Q(voucher__exact='')).filter(survey_id__in=SurveyLogin.objects.filter(work_status=1)).count()
        pendingemponboard =Surveyinfo.objects.filter(~Q(order_id__exact='') | ~Q(voucher__exact='')).filter(survey_id__in=SurveyLogin.objects.filter(work_status=0)).count()

        return render(request,'admin/HiringInfo.html',{'pendingemponboard':pendingemponboard,'totalemponboard':totalemponboard,'pendingempverified':pendingempverified,'totalempverified':totalempverified,'todayregistered':todayregistered,'totalregisterd':totalregistered})
    except Exception as e:
        print("Error",e)
        return redirect('admin-login')
    
def HiringView(request,id):
    try:
        
        result = request.session['ADMIN']
        if id==1:
            temp=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact=""))
            t=temp.filter(Q(created_at=datetime.date.today())).select_related('survey_id')
            
        if id==2:
            t=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).select_related('survey_id')
            
        if id==3:
            t = Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).filter(Q(profile_img_status=1) & Q(aadhar_front_uri_status=1) & Q(aadhar_back_uri_status=1) & Q(driving_licence_status=1) & Q(full_size_img_status=1) & Q(college_id_img_status=1) & Q(tenth_img_status=1) & Q(twelth_img_status=1) & Q(address_img_status=1) & Q(vaccination_img_status=1) & Q(police_verification_img_status=1) & Q(semester_img_status=1))            
            
        if id==4:
            t=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).filter(~Q(profile_img_status=1) & ~Q(aadhar_front_uri_status=1) & ~Q(aadhar_back_uri_status=1) & ~Q(driving_licence_status=1) & ~Q(full_size_img_status=1) & ~Q(college_id_img_status=1) & ~Q(tenth_img_status=1) & ~Q(twelth_img_status=1) & ~Q(address_img_status=1) & ~Q(vaccination_img_status=1) & ~Q(police_verification_img_status=1) & ~Q(semester_img_status=1))        
        if id==5:
            t=Surveyinfo.objects.filter(~Q(order_id__exact='') | ~Q(voucher__exact='')).filter(survey_id__in=SurveyLogin.objects.filter(work_status=1))
        if id==6:
            t=Surveyinfo.objects.filter(~Q(order_id__exact='') | ~Q(voucher__exact='')).filter(survey_id__in=SurveyLogin.objects.filter(work_status=0))
        return render(request,'admin/HiringView.html',{'t':t})
   
    except Exception as e:
        print(e)
        return redirect('admin-login')



def FetchAllClgName(request):
  try:
    q=College.objects.all().values_list("id","name")
    print(q) 
    return JsonResponse({"data": json.dumps(q)},safe=False)
    #return JsonResponse(q,safe=False)
  except Exception as e:
      print(e)
      return JsonResponse([],safe=False)
