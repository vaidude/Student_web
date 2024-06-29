"""
URL configuration for feedback_form project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('home1/',views.home1,name='home1'),
    path('home2/',views.home2,name='home2'),
    path('login1/',views.login1,name='login1'),
    path('login2/',views.login2,name='login2'),
    path('register1/',views.register1,name='register1'),
    path('sfeedback/',views.list_questions,name='sfeedback'),
    path('vfeedback/',views.Vfeedback,name='vfeedback'),
    path('student_list/',views.student_list,name='student_list'),
    path('teacher_list/',views.teacher_list,name='teacher_list'),
    path('delete_record/<int:id>',views.delete_record,name='delete_record'),
    path('delete_record1/<int:id>',views.delete_record1,name='delete_record1'),
    path('dltbyname/',views.dltbyname,name='dltbyname'),
    path('complaint/',views.Complaint,name='complaint'),
    path('profile/',views.profile,name='profile'),
    path('profile1/',views.profile1,name='profile1'),
    path('profile2/',views.profile2,name='profile2'),
    path('register2/',views.register2,name='register2'),
    path('steacher/',views.Steacher,name='steacher'),
    path('un/',views.Un,name='un'),
    path('mq/',views.AddQuestionView,name='mq'),
    path('mc/',views.Mc,name='mc'),
    path('mf/',views.Mf,name='mf'),
    path('ms/',views.Ms,name='ms'),
    path('mt/',views.Mt,name='mt'),
    path('profileupdate/',views.updateuser_profile,name='profileupdate'),
    path('pu1/',views.updateuser_profile1,name='pu1'),
    path('pu2/',views.updateuser_profile2,name='pu2'),
    path('QuestionList/',views.list_questions,name='QuestionList'),
    path('questionUpdate/<qid>/',views.addfeedback_view,name='questionUpdate'),


    path('pie_chart/<int:question_id>/', views.view_pie_chart, name='pie_chart'),
    path('qlist/',views.qlist,name="qlist"),
    path('listcomplaints/',views.complaintlist,name="listcomplaints"),
    path('del-feedback/<id>/',views.DeleteFeedBack,name='del-feedback'),
    path('delete-comp/<id>/',views.DeleteComplaintView,name='delete-comp'),
   
]