from django.shortcuts import render,redirect
from . models import student
from . models import teacher
from . models import hod,Questions
# from . models import product
from . models import complaint
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    return render(request,'index.html')
def home(request):
    StudentName=request.session['username']
    return render(request,'home.html')
def home1(request):
    Name=request.session['username']
    return render(request,'home1.html')
def home2(request):
    Name=request.session['username']
    return render(request,'home2.html')
def login(request):
    if request.method=='POST':

        name = request.POST.get('username')
        pwd = request.POST.get('password')
        cr = student.objects.filter(StudentName=name,Password=pwd)
        if cr:
            userd = student.objects.get(StudentName=name,Password=pwd)
            id=userd.id
            name=userd.StudentName
            pwd=userd.Password
            request.session['id']=id
            request.session['username']=name
            request.session['password']=pwd
            return redirect('home')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

# def home(request):
#     return render(request,'home')
def login1(request):
    if request.method=='POST':

        name = request.POST.get('username')
        pwd = request.POST.get('password')
        print ('username is',name)
        cr = teacher.objects.filter(Name=name,Password=pwd)
        if cr:
            userd = teacher.objects.get(Name=name,Password=pwd)
            id=userd.id
            name=userd.Name
            pwd=userd.Password
            request.session['id']=id
            request.session['username']=name
            request.session['password']=pwd
            return render(request,'home1.html')
        else:
            return render(request,'login1.html')
    else:
        return render(request,'login1.html')

def login2(request):
    if request.method=='POST':

        namE = request.POST.get('username')
        pwD = request.POST.get('password')
        print ('username is',namE)
        cr = hod.objects.filter(Name=namE,Password=pwD)
        if cr:
            userd = hod.objects.get(Name=namE,Password=pwD)
            id=userd.id
            namE=userd.Name
            pwD=userd.Password
            request.session['id']=id
            request.session['username']=namE
            request.session['password']=pwD
            return render(request,'home2.html')
        else:
            return render(request,'login2.html')
    else:
        return render(request,'login2.html')




def register1(request):
    if request.method=="POST":
        NAME= request.POST.get('Name')
        EMAIL= request.POST.get('Email')
        COURSE_CODE = request.POST.get('Course_code')
        COURSE = request.POST.get('Course')
        USERNAME = request.POST.get('username')
        PASSWORD = request.POST.get('password')
        teacher(Name=NAME,Email=EMAIL,Course_code=COURSE_CODE,Course=COURSE,Password=PASSWORD).save()
        return render(request,'login1.html')
    else:
        return render(request,'register1.html')

def register2(request):
    if request.method=="POST":
        NAMe= request.POST.get('Name')
        EMAIl= request.POST.get('Email')
        departmenT = request.POST.get('Department')
        USERNAMe = request.POST.get('username')
        PASSWORd = request.POST.get('password')
        hod(Name=NAMe,Email=EMAIl,Department=departmenT,Password=PASSWORd).save()
        return render(request,'login2.html')
    else:
        return render(request,'register2.html')

def register(request):
    if request.method=="POST":
        name = request.POST.get('Student_Name')
        email = request.POST.get('Student_Email')
        rollno = request.POST.get('Roll_Number')
        branch = request.POST.get('Branch')
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        student(StudentName=name,Email=email,RollNumber=rollno,Branch=branch,Password=password).save()
        return render(request,'login.html')
    else:
        return render(request,'register.html')
def student_list(request):
    students = student.objects.all()
    return render(request, 'student_list.html', {'students':students})
def teacher_list(request):
    teachers = teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers':teachers})
def delete_record(request,id):
    student1 = student.objects.get(id=id)
    student1.delete()
    return render(request,'student_list.html')
def delete_record1(request,id):
    teacher1 = teacher.objects.get(id=id)
    teacher1.delete()
    return render(request,'teacher_list.html')


def dltbyname(request):
    if request.method=="POST":
        name = request.POST.get("cname")
        user = student.objects.get(StudentName=name)
        user.delete()
        return render(request,'student_list.html')
    else:
        return render(request,'dltbyname.html')
# def profile(request):
#     StudentName=request.session['username']
#     data=student.objects.get(StudentName=StudentName)
#     StudentName=data.StudentName
#     RollNumber=data.RollNumber
#     Email=data.Email
#     Branch=data.Branch
#     Password=data.Password
#     return render(request,'profile.html',{'StudentName':StudentName,'RollNumber':RollNumber,'Email':Email,'Branch':Branch,'Password':Password})
def profile1(request):
    Name=request.session['username']
    data=teacher.objects.get(Name=Name)
    Name=data.Name
    Email=data.Email
    Course_code=data.Course_code
    Course=data.Course
    Password=data.Password
    return render(request,'profile1.html',{"Name":Name,"Email":Email,"Course_code":Course_code,"Course":Course,"Password":Password})
def updateuser_profile1(request):
    if request.method =='POST':
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Course_code=request.POST.get('Course_code')
        Course=request.POST.get('Course')
        Password=request.POST.get('password')
        print(Course_code)
        dv=teacher.objects.get(Course_code=Course_code)
        dv.Name=Name
        dv.Email=Email
        dv.Course_code=Course_code
        dv.Course=Course
        dv.Password=Password
        dv.save()
        return render(request, 'home1.html')
    else:
        return render(request, 'profile1.html')
def profile2(request):
    Name=request.session['username']
    data=hod.objects.get(Name=Name)
    Name=data.Name
    Email=data.Email
    Department=data.Department
    Password=data.Password
    return render(request,'profile2.html',{"Name":Name,"Email":Email,"Department":Department,"password":Password})
def updateuser_profile2(request):
    if request.method =='POST':
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Department=request.POST.get('Department')
        Password=request.POST.get('password')
        print(Department)
        de=hod.objects.get(Department=Department)
        de.Name=Name
        de.Email=Email
        de.Department=Department
        de.Password=Password
        de.save()
        return render(request, 'home2.html')
    else:
        return render(request, 'profile2.html')
# def products(request):
#     cr=product.objects.all()
#     return render(request,'product.html',{'product':cr})





def Vfeedback(request):
     return render(request,'vfeedback.html')
def Sfeedback(request):
    return render(request,'sfeedback.html')
def Steacher(request):
    tea = teacher.objects.all()
    return render(request,'steacher.html',{'tea':tea})
def Un(request):
    return render(request,'un.html')
def Mq(request):
    return render(request,'mq.html')
def Mc(request):
    return render(request,'mc.html')
def Mf(request):
    return render(request,'mf.html')
def Mt(request):
    return render(request,'mt.html')
def Ms(request):
    return render(request,'ms.html')
    
# def profileupdate(request):
#     name=request.session['username']
#     data=student.objects.get(name=name)
#     StudentName =data.StudentName 
#     RollNumber=data.RollNumber
#     Email=data.Email
#     Branch=data.Branch
#     Password=data.Password
#     return render(request,'profileupdate.html',{"StudentName":StudentName,"RollNumber":RollNumber,"Email":Email,"Branch":Branch,"Password":Password})







def profile(request):
    name=request.session['username']
    data=student.objects.get(StudentName=name)
    StudentName =data.StudentName 
    RollNumber=data.RollNumber
    Email=data.Email
    Branch=data.Branch
    Password=data.Password
    return render(request,'profile.html',{"StudentName":StudentName,"RollNumber":RollNumber,"Email":Email,"Branch":Branch,"Password":Password})

def updateuser_profile(request):
    if request.method =='POST':
        StudentName=request.POST.get('Student_Name')
        RollNumber= request.POST.get('Roll_Number')
        Email=request.POST.get('Student_Email')
        Branch=request.POST.get('Branch')
        Password=request.POST.get('Password')
        print(RollNumber)
        dt=student.objects.get(RollNumber=RollNumber)
        dt.StudentName=StudentName
        dt.RollNumber=RollNumber
        dt.Email=Email
        dt.Branch=Branch
        dt.Password=Password
        dt.save()
        return render(request, 'home.html')
    else:
        return render(request, 'profile.html')# Create your views here.



def AddQuestionView(request):
    if request.method == 'POST':
        question= request.POST.get('question')

        q=Questions()
        q.question=question
        q.save()
        return redirect('home2')
    else:
        return render(request, 'mq.html')

def list_questions(request):
    question = Questions.objects.all()
    return render(request, 'QuestionList.html', {'question': question})

def qlist(request):
    question = Questions.objects.all()
    return render(request, 'qlist.html', {'question': question})

def DeleteFeedBack(request,id):
    feed= Questions.objects.get(id=id)
    feed.delete()
    return redirect(qlist)

def addfeedback_view(request, qid):
    if 'id' in request.session:
        sid = request.session['id']
        try:
            std = student.objects.get(id=sid)
        except student.DoesNotExist:
            return redirect('login')  # Assuming 'login' is the name of your login URL pattern

        if request.method == 'POST':
            # Assuming you have a form with an input named 'options'
            selected_option = request.POST.get('options')
            question = Questions.objects.get(pk=qid)
            # Create a new instance for each user's feedback
            new_feedback = Questions(student_dtls=std, question=question.question, options=selected_option)
            new_feedback.save()
            return redirect('QuestionList')  # Redirect to a success page after saving feedback
        else:
            return render(request, 'questionUpdate.html', {'qid': qid})  # Pass qid to the template for reference
    else:
        return redirect('login')





def view_pie_chart(request, question_id):
    # Retrieve the question object based on the question_id
    question = Questions.objects.get(pk=question_id)
    
    # Count occurrences of each option for the specific question
    good_count = Questions.objects.filter(id=question_id, options='good').count()
    average_count = Questions.objects.filter(id=question_id, options='average').count()
    poor_count = Questions.objects.filter(id=question_id, options='poor').count()

    # Pass the option counts to the template
    options_count = {
        'good': good_count,
        'average': average_count,
        'poor': poor_count,
    }
    
    print('Options Count:', options_count)  # Add this line to inspect the options count

    return render(request, 'pie_chart.html', {'options_count': options_count})


def complaintlist(request):
    complaints = complaint.objects.all()
    return render(request, 'listcomplaints.html', {'c':complaints})
 


import smtplib
from email.mime.text import MIMEText
from django.shortcuts import render
from .models import complaint, hod  # Assuming the models are imported from your models file

def Complaint(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        complaint_text = request.POST.get('complaint')

        # Create a new instance of the Complaint model and save it to the database
        new_complaint = complaint(Name=name, email=email, Complaint=complaint_text)
        new_complaint.save()

        # Send email to HOD
        try:
            # Retrieve the HOD email (assuming there's only one HOD for simplicity)
            hod_email = hod.objects.first().Email  # Adjust this according to your actual HOD retrieval logic

            # Prepare the email message
            subject = 'Complaint Submitted'
            message = f'Hello HOD,\n\nA complaint has been submitted by a student.\n\nName: {name}\nEmail: {email}\nComplaint: {complaint_text}\n\nThank you.'

            # Sender and receiver email addresses
            send_mail(
                subject,
                message,
                from_email= settings.EMAIL_HOST_USER,
                recipient_list=[hod_email],
            )

            return render(request, 'home.html')
        except Exception as e:
            # Handle any exceptions (e.g., SMTP authentication error, connection error)
            return HttpResponse(e)
            # return HttpResponse("<div style='display:flex; text-align:center;align-items:center;justify-content:center;padding-top:54vh; font-size:50px;color:red;'>CAN'T ACESS COMPLAINT </div>")
    else:
        return render(request, 'complaint.html')
    
def DeleteComplaintView(request,id):
    comp=complaint.objects.get(id=id)
    comp.delete()
    return redirect('listcomplaints')
    
