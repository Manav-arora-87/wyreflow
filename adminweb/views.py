import json
from django.shortcuts import redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect

# Create your views here.
import os
import bcrypt
import datetime
from django.shortcuts import render
from .models import Adminlogins, SemesterImg, SurveyHistory
from .models import Surveyinfo,State,District,Block,Village
from .models import SurveyLogin
from adminweb.models import College
from django.db.models import Q
from django.urls import reverse
from django.views.decorators.cache import cache_control
import math
from django.core.cache import cache

from decouple import config



def Login(request):
    try:
        result = request.session['ADMIN']
        
        return redirect("admin-dashboard")
       # return render(request, "admin/Dashboard.html",{'result':res})
    except Exception as e:
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
        if param!=None:
            t,year,clgname,type=SearchingData(request,id)
        else:
         t=hiringview_data(id)
        return render(request,'admin/HiringView.html',{'t':t,'id':id,'clgname':clgname,'year':year,'type':type,'imgurl':config("imgurl")})
   
    except Exception as e:
        print(e)
        # Logout(request) 
        return redirect('admin-login')



def FetchAllClgName(request):
  try:
    q=College.objects.all().values("id","name")
    return JsonResponse({"data": list(q)},safe=False)
    #return JsonResponse(q,safe=False)
  except Exception as e:
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
        return [],0,0,0

import datetime
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def SurveyUserView(request,empid):
    try:
        result = request.session['ADMIN']
        request.session['id']=empid
        t=Surveyinfo.objects.filter(Q(survey_id__exact=empid)).extra({'state':'select state_name from state where state_id =surveyinfo.assign_state','district':'select dist_name from district where state_id =surveyinfo.assign_state and dist_id = surveyinfo.assign_dist','block':'select block_name from block where state_id =surveyinfo.assign_state and dist_id = surveyinfo.assign_dist and block_id = surveyinfo.assign_block','village':'select village_name from village where state_id =surveyinfo.assign_state and dist_id = surveyinfo.assign_dist and block_id = surveyinfo.assign_block and village_id = surveyinfo.assign_village'})
        res=SurveyHistory.objects.filter(Q(survey_id__exact=empid))
       
        d={}
        if  res !=None:
            for index,i in enumerate(res):
                a=int(i.end_time) 
                b=int(i.start_time)
                time=(a-b)/1000
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
                setattr(i,"total_time",temp) 
        state=fetchallstates()    
        

        return render(request, "admin/SurveyUserView.html",{'id':empid,'t':t,'res':res,'d':d,'imgurl':config("imgurl"),'states':state})
    except  Exception as e:
        print(e)
        # Logout(request) 
        return redirect('admin-login')


def checkdoc(doc):
    try:
         imgext=['.png','.jpg' , '.jpeg', '.jfif','.pjpeg', '.pjp','.gif']
         pdfext=['.pdf']
         doc,fileext= os.path.splitext(doc)
         if fileext in imgext:
             return 1 #image file
         elif fileext in pdfext:
             return 2 #pdf file
         else:
             return 3  #invalid file
    except:
        return 3          
               
def surveyor_data(id):
        t=Surveyinfo.objects.filter(Q(survey_id=id))
        semimg=SemesterImg.objects.filter(survey_id=id)
        for i in t:
            status_driv=checkdoc(i.driving_licence_img)
            setattr(i,"dl_type",status_driv)
            status_driv=checkdoc(i.full_size_img)
            setattr(i,"fs_type",status_driv)
            status_driv=checkdoc(i.college_id_img)
            setattr(i,"ci_type",status_driv)
            status_driv=checkdoc(i.tenth_img)
            setattr(i,"th_type",status_driv)
            status_driv=checkdoc(i.twelth_img)
            setattr(i,"tw_type",status_driv)
            status_driv=checkdoc(i.address_img)
            setattr(i,"add_type",status_driv)
            status_driv=checkdoc(i.vaccination_img)
            setattr(i,"vac_type",status_driv)
            status_driv=checkdoc(i.police_verification_img)
            setattr(i,"pvr_type",status_driv)
        for i in semimg:
            status_driv=checkdoc(i.img_name)
            setattr(i,"sem_type",status_driv)            
        return t,semimg     

def ShowDocuments(request):
    try:
        result = request.session['ADMIN']
        t,semimg=surveyor_data(request.session['id'])

        semlength=len(semimg)
        return render(request, "admin/ShowDocuments.html",{'semlength':semlength,'id':id,'t':t,'semimg':semimg, 'profileimgurl':config("imgurl"),'aadharimgurl':config("aadhar"),'url':config('url')})
        
    except  Exception as e:
        Logout(request) 
        return redirect('admin-login')  


def DocumentStatus(request):
    try:
        result = request.session['ADMIN']
        if request.is_ajax and request.method == "POST":
            pimg = request.POST.get('pimg',None)
            afimg = request.POST.get('afimg',None)
            abimg = request.POST.get('abimg',None)
            drimg = request.POST.get('drimg',None)
            fsimg = request.POST.get('fsimg',None)
            ciimg = request.POST.get('ciimg',None)
            thimg = request.POST.get('thimg',None)
            twimg =request.POST.get('twimg',None)
            addimg = request.POST.get('addimg',None)
            vacimg = request.POST.get('vacimg',None)
            pvrimg = request.POST.get('pvrimg',None)
            semesterimg = request.POST.get('semesterimg',None)
            t8=Surveyinfo.objects.filter(Q(survey_id=request.session['id'])).update(semester_img_status= semesterimg,profile_img_status= pimg,aadhar_front_uri_status=afimg,aadhar_back_uri_status=abimg,driving_licence_status=drimg,full_size_img_status=fsimg,college_id_img_status=ciimg,tenth_img_status=thimg,twelth_img_status=twimg,address_img_status=addimg,vaccination_img_status=vacimg,police_verification_img_status=pvrimg)

            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
 


def update_verfication(request):
    try:
        result = request.session['ADMIN']
        if request.is_ajax and request.method == "POST":
            status=None
            if request.POST['data']=="0":
                status=1
            else:
                status=0
            SurveyLogin.objects.filter(survey_registration_id=request.POST['regid']).update(verified_status=status)       
            return JsonResponse({"status": "done"}, status=200)

        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
 

def fetchallstates():
    try:
       t=State.objects.all().values("state_id","state_name")
       print(t)
       return t
       
       #return JsonResponse(t,safe=False)
    except Exception as e:
      print("Errrrrrr",e)
      return []


def fetchalldistricts(request):
    try:
     if request.is_ajax and request.method == "POST":
         print(request.POST['id'])
    #    t=District.objects.filter(Q(state_id = id))
    #    return JsonResponse(t,safe=False)
    except Exception as e:
      print(e)
      return JsonResponse([],safe=False)

def fetchallblocks(request):
    try:
       t=Block.objects.all()
       return JsonResponse(t,safe=False)
    except Exception as e:
      print(e)
      return JsonResponse([],safe=False)

def fetchallvillages(request):
    try:
       t=Village.objects.all()
       return JsonResponse(t,safe=False)
    except Exception as e:
      print(e)
      return JsonResponse([],safe=False)
