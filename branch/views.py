from django.http import HttpResponse
from django.shortcuts import render
from branch.models import bhayander_kinderGarten_english,bhayander_primary_english,bhayander_secondary_english,bhayander_juniorCollege,bhayander_achivement,bhayander_event,bhayander_facility,bhayander_management
from branch.models import bhayander_kinderGarten_hindi,bhayander_primary_hindi,bhayander_secondary_hindi
from branch.models import bhayander_juniorCollege_teacher,bhayander_kinderGarten_english_teacher,bhayander_kinderGarten_hindi_teacher,bhayander_primary_english_teacher,bhayander_primary_hindi_teacher,bhayander_secondary_english_teacher,bhayander_secondary_hindi_teacher
from branch.models import nalasopara_kinderGarten,nalasopara_primary_english,nalasopara_achivement,nalasopara_event,nalasopara_facility,nalasopara_management
from branch.models import nalasopara_primary_hindi,nalasopara_secondary_hindi
from branch.models import nalasopara_kinderGarten_teacher,nalasopara_primary_english_teacher,nalasopara_primary_hindi_teacher,nalasopara_secondary_hindi_teacher
from branch.models import virar_achivement,virar_event,virar_facility,virar_management
from branch.models import virar_primary_hindi,virar_secondary_hindi
from branch.models import virar_primary_hindi_teacher,virar_secondary_hindi_teacher
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse 
from django.conf import settings
# Create your views here.

def branch_url_redirect(request):
    
    return HttpResponseRedirect(reverse('dashboard'))


def bhayander_index(request):
    achived=bhayander_achivement.objects.all()
    events=bhayander_event.objects.all()
    facilities=bhayander_facility.objects.all()
    managements=bhayander_management.objects.all()
    return render(request,'branch_home/bhayander_index.html',{'achived':achived,'events':events,'facilities':facilities,'managements':managements})

def nalasopara_index(request):
    achived=nalasopara_achivement.objects.all()
    events=nalasopara_event.objects.all()
    facilities=nalasopara_facility.objects.all()
    managements=nalasopara_management.objects.all()
    return render(request,'branch_home/nalasopara_index.html',{'achived':achived,'events':events,'facilities':facilities,'managements':managements})

def virar_index(request):
    achived=virar_achivement.objects.all()
    events=virar_event.objects.all()
    facilities=virar_facility.objects.all()
    managements=virar_management.objects.all()
    return render(request,'branch_home/virar_index.html',{'achived':achived,'events':events,'facilities':facilities,'managements':managements})

def bhayander_course_kinderGarten(request):
    obj=bhayander_kinderGarten_english.objects.all()
    obj1=bhayander_kinderGarten_hindi.objects.all()
    teacher=bhayander_kinderGarten_english_teacher.objects.all()
    teacher1=bhayander_kinderGarten_hindi_teacher.objects.all()
    return render(request,'branch_home/bhayander_course_kinderGarten.html',{'obj':obj,'obj1':obj1,'teacher':teacher,'teacher1':teacher1})


def bhayander_course_primary(request):
    obj=bhayander_primary_english.objects.all()
    obj1=bhayander_primary_hindi.objects.all()
    teacher=bhayander_primary_english_teacher.objects.all()
    teacher1=bhayander_primary_hindi_teacher.objects.all()
    return render(request,'branch_home/bhayander_course_primary.html',{'obj':obj,'obj1':obj1,'teacher':teacher,'teacher1':teacher1})

def bhayander_course_secondary(request):
    obj=bhayander_secondary_english.objects.all()
    obj1=bhayander_secondary_hindi.objects.all()
    teacher=bhayander_secondary_english_teacher.objects.all()
    teacher1=bhayander_secondary_hindi_teacher.objects.all()
    return render(request,'branch_home/bhayander_course_secondary.html',{'obj':obj,'obj1':obj1,'teacher':teacher,'teacher1':teacher1})

def bhayander_course_college(request):
    obj=bhayander_juniorCollege.objects.all()
    teacher=bhayander_juniorCollege_teacher.objects.all()
     
    return render(request,'branch_home/bhayander_course_college.html',{'obj':obj,'teacher':teacher})


def nalasopara_course_primary(request):
    obj=nalasopara_primary_english.objects.all()
    obj1=nalasopara_primary_hindi.objects.all()
    teacher=nalasopara_primary_english_teacher.objects.all()
    teacher1=nalasopara_primary_hindi_teacher.objects.all()
    return render(request,'branch_home/nalasopara_course_primary.html',{'obj':obj,'obj1':obj1,'teacher':teacher,'teacher1':teacher1})

def nalasopara_course_secondary(request):
    
    obj1=nalasopara_secondary_hindi.objects.all()
    
    teacher1=nalasopara_secondary_hindi_teacher.objects.all()
    print(teacher1)
    return render(request,'branch_home/nalasopara_course_secondary.html',{'obj1':obj1,'teachers1':teacher1})

def nalasopara_course_kinderGarten(request):
    obj=nalasopara_kinderGarten.objects.all()
    teacher=nalasopara_kinderGarten_teacher.objects.all()
    return render(request,'branch_home/nalasopara_course_kinderGarten.html',{'obj':obj,'teacher':teacher})

def virar_course_primary(request):
     
    obj1=virar_primary_hindi.objects.all()
    teacher=virar_primary_hindi_teacher.objects.all()
    return render(request,'branch_home/virar_course_primary.html',{'obj1':obj1,'teacher':teacher})

def virar_course_secondary(request):
     
    obj1=virar_secondary_hindi.objects.all()
    teacher=virar_secondary_hindi_teacher.objects.all()
    return render(request,'branch_home/virar_course_secondary.html',{'obj1':obj1,'teacher':teacher})

