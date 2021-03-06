"""wyreflowtask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adminweb import  views
# r

urlpatterns = [
    # path('adminweb/', adminweb.site.urls),

    path('admin-login/',views.Login,name='admin-login'),
    path('admin-checklogin',views.CheckAdminLogin),
    path('admin-hiringinfo/',views.HiringInfo),
    path('admin-dashboard/',views.Admindashboard,name='admin-dashboard'),
    path('admin-hiringview/<int:id>',views.HiringView,name='admin-hiringview'),
    path('fetchallclgname/',views.FetchAllClgName),
    path('searchingdata/<int:id>',views.SearchingData),
    path('admin-surveyuserview/<int:empid>',views.SurveyUserView,name='admin-surveyuserview'),
    path('admin-showdocuments/',views.ShowDocuments,name='admin-showdocuments'),
    path('admin-update_surveyor_doc',views.DocumentStatus,name='admin-update_surveyor_doc'),
    path('admin-update_surveyor_verfications',views.update_verfication,name='admin-update_surveyor_verfications'),
    path('fetchalldistricts',views.fetchalldistricts,name='fatchalldistricts'),
    path('fetchallblocks',views.fetchallblocks,name='fatchallblocks'),
    path('fetchallvillages',views.fetchallvillages,name='fatchallvillages'),
    path('setsurveylocation',views.setsurveylocation,name='setsurveylocation'),

]
