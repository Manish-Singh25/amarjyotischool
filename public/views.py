from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from public.models import teacher_join,student_join,login_admin,alumni,achivement,event,facility,management
from django.urls import reverse #we used reverse function to use name instead of a url in urls.py
from branch import urls
from django.contrib.auth.models import User
# Create your views here.


def url_redirect(request):
    
    return HttpResponseRedirect(reverse('dashboard'))

def dashboard(request):
    achived=achivement.objects.all()
    events=event.objects.all()
    facilities=facility.objects.all()
    managements=management.objects.all()
    return render(request,'public_dashboard/index.html',{'achived':achived,'events':events,'facilities':facilities,'managements':managements})


def alumini(request):
    detail=alumni.objects.all()

    return render(request,'public_dashboard/alumini.html',{'detail':detail})


def joinUs(request):
    return render(request,'public_dashboard/joinUs.html')

def aboutUs(request):
    managements=management.objects.all()
    return render(request,'public_dashboard/aboutUs.html',{'managements':managements})

def contactUs(request):
    return render(request,'public_dashboard/contact.html')

def login(request):
    return render(request,'public_dashboard/login.html')

def authenticate(request):
    username=request.POST['l_email']
    password=request.POST['l_pass']
    auth=login_admin.objects.filter(username=username,password=password)

    if len(auth):
        request.session['username']=username
        return HttpResponseRedirect(reverse('admin_index'))
    else:
        return HttpResponseRedirect(reverse('login')+'?login=False')

def students_join(request):
    first_name=request.POST['s_first']
    last_name=request.POST['s_last']
    father_name=request.POST['s_father']
    mother_name=request.POST['s_mother']
    father_email=request.POST['s_fatherEmail']
    father_contact=request.POST['s_fatherContact']
    mother_email=request.POST['s_motherEmail']
    mother_contact=request.POST['s_motherContact']

    uplode=student_join(first_name=first_name,last_name=last_name,father_name=father_name,mother_name=mother_name,father_email=father_email,father_contact=father_contact,mother_email=mother_email,mother_contact=mother_contact)
    uplode.save()
    return HttpResponseRedirect(reverse('joinUs')+'?uplode=True')

def teachers_join(request):
    first_name=request.POST['t_first']
    last_name=request.POST['t_last']
    email=request.POST['t_email']
    contact=request.POST['t_contact']
    qualification=request.POST['t_qualifications']
    post=request.POST['t_post']
    experience=request.POST['t_experience']
    last_school=request.POST['t_lastSchool']

    uplode=teacher_join(first_name=first_name,last_name=last_name,email=email,contact=contact,qualification=qualification,post=post,experience=experience,last_school=last_school)
    uplode.save()
    return HttpResponseRedirect(reverse('joinUs')+'?uplode=True')

def signup(request):
    first_name=request.POST['s_first']
    last_name=request.POST['s_last']
    email=request.POST['s_email']
    password=request.POST['s_pass']
    count=login_admin.objects.count()

    if count>0:
        return HttpResponseRedirect(reverse('login')+'?success1=False') 
    else:
        uplode=login_admin(first_name=first_name,last_name=last_name,username=email,password=password)
        uplode.save()
        return HttpResponseRedirect(reverse('login')+'?success=True')
