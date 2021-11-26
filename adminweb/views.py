import json
from django.shortcuts import redirect
from django.http import JsonResponse
# Create your views here.
import os
import bcrypt
import datetime
from django.shortcuts import render
from .models import Adminlogins, SurveyHistory
from .models import Surveyinfo
from .models import SurveyLogin
from adminweb.models import College
from django.db.models import Q
from django.urls import reverse
from django.views.decorators.cache import cache_control
import math


def Login(request):
    try:
        result = request.session['ADMIN']
        
       # print(result)
        return redirect("admin-dashboard")
       # return render(request, "admin/Dashboard.html",{'result':res})
    except Exception as e:
        print("Error",e)
        return render(request,'admin/Login.html')


def Logout(request):
    request.session.flush()
    #del request.session['ADMIN']
    #return redirect("admin-login")


def CheckAdminLogin(request):
    # SurveyLogin.objects.({'hisdf':""})

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
          #print(e)
          Logout(request) 
          return render(request, "admin/Login.html", {'msg': 'Server Error'})

def Admindashboard(request):
    try:
        result = request.session['ADMIN']
        res = Surveyinfo.objects.filter(~Q(order_id__exact="") | ~Q(voucher__exact="")).count()

        return render(request, "admin/Dashboard.html", {'result': res})
    except  Exception as e:
        Logout(request) 
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
        Logout(request) 
        return redirect('admin-login')
    
def hiringview_data(id):
        if id==1:
            temp=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact=""))
            t=temp.filter(Q(created_at=datetime.date.today())).select_related('survey_id')
            
        elif id==2:
            t=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).select_related('survey_id')
            
        elif id==3:
            t = Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).filter(Q(profile_img_status=1) & Q(aadhar_front_uri_status=1) & Q(aadhar_back_uri_status=1) & Q(driving_licence_status=1) & Q(full_size_img_status=1) & Q(college_id_img_status=1) & Q(tenth_img_status=1) & Q(twelth_img_status=1) & Q(address_img_status=1) & Q(vaccination_img_status=1) & Q(police_verification_img_status=1) & Q(semester_img_status=1))            
            
        elif id==4:
            t=Surveyinfo.objects.filter(~Q(order_id__exact="")|~Q(voucher__exact="")).filter(~Q(profile_img_status=1) & ~Q(aadhar_front_uri_status=1) & ~Q(aadhar_back_uri_status=1) & ~Q(driving_licence_status=1) & ~Q(full_size_img_status=1) & ~Q(college_id_img_status=1) & ~Q(tenth_img_status=1) & ~Q(twelth_img_status=1) & ~Q(address_img_status=1) & ~Q(vaccination_img_status=1) & ~Q(police_verification_img_status=1) & ~Q(semester_img_status=1))        
        elif id==5:
            t=Surveyinfo.objects.filter(~Q(order_id__exact='') | ~Q(voucher__exact='')).filter(survey_id__in=SurveyLogin.objects.filter(work_status=1))
        elif id==6:
            t=Surveyinfo.objects.filter(~Q(order_id__exact='') | ~Q(voucher__exact='')).filter(survey_id__in=SurveyLogin.objects.filter(work_status=0))
        return t

def HiringView(request,id):
    try:
        
        result = request.session['ADMIN']
        t=[]
        year=0
        clgname=0
        type=0
        param=request.GET.get('param',None)
        # print(param)
        if param!=None:
            t,year,clgname,type=SearchingData(request,id)
           # print(year,clgname,type)
        else:
         t=hiringview_data(id)
        # print(t) 
        return render(request,'admin/HiringView.html',{'t':t,'id':id,'clgname':clgname,'year':year,'type':type})
   
    except Exception as e:
        print(e)
        Logout(request) 
        return redirect('admin-login')



def FetchAllClgName(request):
  try:
    q=College.objects.all().values("id","name")
    #print(q) 
    return JsonResponse({"data": list(q)},safe=False)
    #return JsonResponse(q,safe=False)
  except Exception as e:
      print(e)
      return JsonResponse([],safe=False)


def SearchingData(request,id):
    try:
        year=request.POST['year']
        clgname=request.POST['clgname']
        type=request.POST['type']
        if year=='0' and clgname =='0' and type=='0':
            res=hiringview_data(id)
        elif clgname =='0' and type=='0':
            res=hiringview_data(id)
            res=res.filter(Q(passing_year=year))
        elif year=='0' and clgname =='0':
            res=hiringview_data(id)
            if(type=="1"):
                res=res.filter(~Q(order_id__exact=''))
            else:
                res=res.filter(~Q(voucher__exact=''))    
        elif year=='0'  and type=='0':
            res=hiringview_data(id)
            res=res.filter(Q(college_name=clgname))
        elif  clgname =='0':
            res=hiringview_data(id)
            if(type=="1"):
                res=res.filter(~Q(order_id__exact='')).filter(Q(passing_year=year))
            else:
                res=res.filter(~Q(voucher__exact='')).filter(Q(passing_year=year))

        elif year=='0':
            res=hiringview_data(id)
            if(type=="1"):
                res=res.filter(~Q(order_id__exact='')).filter(Q(college_name=clgname))
            else:
                res=res.filter(~Q(voucher__exact='')).filter(Q(college_name=clgname))
        elif type=='0':
            res=hiringview_data(id)
            res=res.filter(Q(college_name=clgname)).filter(Q(passing_year=year))
        else:
            res=hiringview_data(id)
            if(type=="1"):
                res=res.filter(~Q(order_id__exact='')).filter(Q(college_name=clgname)).filter(Q(passing_year=year))
            else:
                res=res.filter(~Q(voucher__exact='')).filter(Q(college_name=clgname)).filter(Q(passing_year=year))

        return res,year,clgname,type

    except Exception as e:
        print(e)
        return [],0,0,0

import datetime
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def SurveyUserView(request,empid):
    try:
        result = request.session['ADMIN']
        print(empid)
        t=Surveyinfo.objects.filter(Q(survey_id__exact=empid)).extra({'state':'select state_name from state where state_id =surveyinfo.assign_state','district':'select dist_name from district where state_id =surveyinfo.assign_state and dist_id = surveyinfo.assign_dist','block':'select block_name from block where state_id =surveyinfo.assign_state and dist_id = surveyinfo.assign_dist and block_id = surveyinfo.assign_block','village':'select village_name from village where state_id =surveyinfo.assign_state and dist_id = surveyinfo.assign_dist and block_id = surveyinfo.assign_block and village_id = surveyinfo.assign_village'})
        res=SurveyHistory.objects.filter(Q(survey_id__exact=empid))
        #   time=(end_time-start_time)/1000;
        #  cal=Math.floor(time/60);
        #   se=String(Math.floor(time%60));
        #  m=String(cal%60);
        #  h=String(Math.floor(cal/60));
        #  hDisplay = h > 0 ? (h.length>1? h+":":"0"+h+":"): "00:";
        #  mDisplay = m > 0 ? (m.length>1?m+":":"0"+m+":"): "00:";
        #  sDisplay = se > 0 ? (se.length>1?se:"0"+se) : "00";
        #  ntime= hDisplay + mDisplay + sDisplay;
        # // console.log(ntime)
        # return ntime;
        d={}
        if  res !=None:
            for index,i in enumerate(res):
                a=int(i.end_time) 
                b=int(i.start_time)
                time=(a-b)/1000
                print(time)
                cal=math.floor(time/60)
                se=str(math.floor(time%60))
                m=str(cal%60)
                h=str(math.floor(cal/60))
                if(len(se)==1):
                    se="0"+se
                if(len(m)==1):
                    m="0"+m
                if(len(h)==1):
                    h="0"+h
                temp=h+":"+m+":"+se 
                d[index+1]=temp  


           
        print(d)
        return render(request, "admin/SurveyUserView.html",{'t':t,'res':res,'d':d})
    except  Exception as e:
        print("Error",e)
        Logout(request) 
        return redirect('admin-login')

def ShowDocuments(request):
    try:
        result = request.session['ADMIN']
        return render(request, "admin/ShowDocuments.html")
    except  Exception as e:
        print("Error",e)
        Logout(request) 
        return redirect('admin-login')    