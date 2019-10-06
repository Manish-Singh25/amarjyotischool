from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from public.models import achivement,alumni,event,facility,student_join,teacher_join,login_admin,management
from branch.models import bhayander_achivement,bhayander_event,bhayander_facility,bhayander_juniorCollege,bhayander_kinderGarten_english,bhayander_primary_english,bhayander_secondary_english,bhayander_management
from branch.models import bhayander_kinderGarten_hindi,bhayander_primary_hindi,bhayander_secondary_hindi
from branch.models import bhayander_juniorCollege_teacher,bhayander_kinderGarten_english_teacher,bhayander_kinderGarten_hindi_teacher,bhayander_primary_english_teacher,bhayander_primary_hindi_teacher,bhayander_secondary_english_teacher,bhayander_secondary_hindi_teacher
from branch.models import nalasopara_achivement,nalasopara_primary_english,nalasopara_event,nalasopara_facility,nalasopara_kinderGarten,nalasopara_management
from branch.models import nalasopara_primary_hindi,nalasopara_secondary_hindi
from branch.models import nalasopara_kinderGarten_teacher,nalasopara_primary_english_teacher,nalasopara_primary_hindi_teacher,nalasopara_secondary_hindi_teacher
from branch.models import virar_achivement,virar_event,virar_facility,virar_management
from branch.models import virar_primary_hindi,virar_secondary_hindi
from branch.models import virar_primary_hindi_teacher,virar_secondary_hindi_teacher
from django.core.files.storage import FileSystemStorage
import os
import sys
from PIL import Image
import copy 
from school.settings import MEDIA_ROOT
from django.urls import reverse #we used reverse function to use name instead of a url in urls.py
# Create your views here.

def admin_url_redirect(request):
    return HttpResponseRedirect(reverse('admin_index'))

def admin_index(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    name=login_admin.objects.filter(username=username)
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    alumnis=alumni.objects.all()
    achive=achivement.objects.all()
    events=event.objects.all()
    facilities=facility.objects.all()
    managements=management.objects.all()
    return render(request,'admin/admin_index.html',{'alumnis':alumnis,'achive':achive,'events':events,'facilities':facilities,'managements':managements,'name':name})

def uplode_admin_index(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    name=login_admin.objects.filter(username=username)
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    return render(request,'admin/add_admin_index.html',{'name':name})

def save_admin_index(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    path=request.POST['add']
    if path=='alumni':
        name=request.POST['alumni_name']
        passout=request.POST['alumni_pass']
        job=request.POST['alumni_job']
        discription=request.POST['alumni_discription']
        image=''
        if request.method=='POST' and request.FILES['alumni_image']:
            myfile=request.FILES['alumni_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        s=alumni(name=name,pass_out=passout,job=job,discription=discription,image=image,url=url)
        s.save()

    elif path=='achive':
        name=request.POST['achive_name']
        achive=request.POST['achive_achive']
        discription=request.POST['achive_discription']
        image=''
        if request.method=='POST' and request.FILES['achive_image']:
            myfile=request.FILES['achive_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        s=achivement(name=name,achive=achive,discription=discription,image=image,url=url)
        s.save()

    elif path=='event':
        name=request.POST['event_name']
        date=request.POST['event_date']
        time=request.POST['event_time']
        discription=request.POST['event_discription']
        image=''
        if request.method=='POST' and request.FILES['event_image']:
            myfile=request.FILES['event_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        s=event(name=name,date=date,time=time,discription=discription,image=image,url=url)
        s.save()

    elif path=='facility':
        name=request.POST['facility_name']
        discription=request.POST['facility_discription']
        image=''
        if request.method=='POST' and request.FILES['facility_image']:
            myfile=request.FILES['facility_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)

        s=facility(name=name,discription=discription,image=image,url=url)
        s.save()
    elif path=='managements':
        name=request.POST['management_name']
        designation=request.POST['management_designation']
        discription=request.POST['management_discription']
        image=''
        if request.method=='POST' and request.FILES['management_image']:
            myfile=request.FILES['management_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)

        s=management(name=name,discription=discription,designation=designation,image=image,url=url)
        s.save()

    return HttpResponseRedirect(reverse('admin_index'))


def delete_alumni(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    id=request.POST['pid']
    if id:
        obj=alumni.objects.filter(id=id)
        for i in obj:
            path=i.url
            print(path)
        path=str(path)
        if os.path.isfile(path):
            os.remove(path)
            
        alumni.objects.filter(id=id).delete()  
    return HttpResponseRedirect(reverse('admin_index'))

def delete_achivement(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    id=request.POST['pid']
    if id:
        obj=achivement.objects.filter(id=id)
        for i in obj:
            path=i.url
            print(path)
        path=str(path)
        if os.path.isfile(path):
            os.remove(path)
        achivement.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('admin_index'))

def delete_event(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    id=request.POST['pid']
    if id:
        obj=event.objects.filter(id=id)
        for i in obj:
            path=i.url
            print(path)
        path=str(path)
        if os.path.isfile(path):
            os.remove(path)
        event.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('admin_index'))

def delete_facility(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    id=request.POST['pid']
     
    if id:
        obj=facility.objects.filter(id=id)
        for i in obj:
            path=i.url
            print(path)
        path=str(path)
        if os.path.isfile(path):
            os.remove(path)
        facility.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('admin_index'))

def delete_management(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    id=request.POST['pid']
     
    if id:
        obj=management.objects.filter(id=id)
        for i in obj:
            path=i.url
            print(path)
        path=str(path)
        if os.path.isfile(path):
            os.remove(path)
        management.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('admin_index'))

def join_request(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    student=student_join.objects.all()
    teacher=teacher_join.objects.all()
    return render(request,'admin/join_request.html',{'student':student,'teacher':teacher})

def delete_student(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    id=request.POST['pid']
    print(id)
    if id:
        student_join.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('join_request'))

def delete_teacher(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    id=request.POST['pid']
    print(id)
    if id:
        teacher_join.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('join_request'))

def logout(request):
    if 'username'  in request.session:
        del request.session['username']
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))

def bhayander_admin_index(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))    
    name=login_admin.objects.filter(username=username) 
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    achive=bhayander_achivement.objects.all()
    events=bhayander_event.objects.all()
    facilities=bhayander_facility.objects.all()
    managements=bhayander_management.objects.all()
    return render(request,'admin/bhayander_admin_index.html',{'achive':achive,'events':events,'facilities':facilities,'name':name,'managements':managements})

def bhayander_admin_kinder_garten(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))    
    name=login_admin.objects.filter(username=username) 
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    obj=bhayander_kinderGarten_english.objects.all()
    obj1=bhayander_kinderGarten_hindi.objects.all()
    teacher=bhayander_kinderGarten_english_teacher.objects.all()
    teacher1=bhayander_kinderGarten_hindi_teacher.objects.all()
    return render(request,'admin/bhayander_admin_kinder_garten.html',{'obj':obj,'obj1':obj1,'name':name,'teacher':teacher,'teacher1':teacher1})

def bhayander_admin_primary(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))    
    name=login_admin.objects.filter(username=username) 
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    obj=bhayander_primary_english.objects.all()
    obj1=bhayander_primary_hindi.objects.all()
    teacher=bhayander_primary_english_teacher.objects.all()
    teacher1=bhayander_primary_hindi_teacher.objects.all()
    return render(request,'admin/bhayander_admin_primary.html',{'obj':obj,'obj1':obj1,'name':name,'teacher':teacher,'teacher1':teacher1})

def bhayander_admin_secondary(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))    
    name=login_admin.objects.filter(username=username) 
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    obj=bhayander_secondary_english.objects.all()
    obj1=bhayander_secondary_hindi.objects.all()
    teacher=bhayander_secondary_english_teacher.objects.all()
    teacher1=bhayander_secondary_hindi_teacher.objects.all()
    return render(request,'admin/bhayander_admin_secondary.html',{'obj':obj,'obj1':obj1,'name':name,'teacher':teacher,'teacher1':teacher1})

def bhayander_admin_college(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))   
    name=login_admin.objects.filter(username=username) 
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    obj=bhayander_juniorCollege.objects.all()
    teacher=bhayander_juniorCollege_teacher.objects.all()
    return render(request,'admin/bhayander_admin_college.html',{'obj':obj,'name':name,'teacher':teacher})

def delete_bhayander(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    try:
        if request.POST['bhayander_index_achivement']:
            id=request.POST['bhayander_index_achivement']
            obj=bhayander_achivement.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_achivement.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_index'))
    except Exception as e:
        print("type error: " + str(e))    
    try:
        if request.POST['bhayander_index_event']:
            id=request.POST['bhayander_index_event']
            obj=bhayander_event.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_event.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_index'))
    except Exception as e:
        print("type error: " + str(e))  
    try:
        if request.POST['bhayander_index_facility']:
            id=request.POST['bhayander_index_facility']
            obj=bhayander_facility.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_facility.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_index'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['bhayander_index_management']:
            id=request.POST['bhayander_index_management']
            obj=bhayander_management.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_management.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_index'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['bhayander_college']:
            id=request.POST['bhayander_college']
            obj=bhayander_juniorCollege.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_juniorCollege.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_college'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['bhayander_college_teacher']:
            id=request.POST['bhayander_college_teacher']
            obj=bhayander_juniorCollege_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_juniorCollege_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_college'))
    except Exception as e:
        print("type error: " + str(e))
    try:
        if request.POST['bhayander_kinder_garten_english']:
            id=request.POST['bhayander_kinder_garten_english']
            obj=bhayander_kinderGarten_english.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_kinderGarten_english.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_kinder_garten'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['bhayander_kinder_garten_english_teacher']:
            id=request.POST['bhayander_kinder_garten_english_teacher']
            obj=bhayander_kinderGarten_english_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_kinderGarten_english_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_kinder_garten'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['bhayander_kinder_garten_hindi']:
            id=request.POST['bhayander_kinder_garten_hindi']
            obj=bhayander_kinderGarten_hindi.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_kinderGarten_hindi.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_kinder_garten'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['bhayander_kinder_garten_hindi_teacher']:
            id=request.POST['bhayander_kinder_garten_hindi_teacher']
            obj=bhayander_kinderGarten_hindi_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_kinderGarten_hindi_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_kinder_garten'))
    except Exception as e:
        print("type error: " + str(e))
    try:
        if request.POST['bhayander_primary_english']:
            id=request.POST['bhayander_primary_english']
            obj=bhayander_primary_english.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_primary_english.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_primary'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['bhayander_primary_english_teacher']:
            id=request.POST['bhayander_primary_english_teacher']
            obj=bhayander_primary_english_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_primary_english_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_primary'))
    except Exception as e:
        print("type error: " + str(e))
    try:
        if request.POST['bhayander_primary_hindi']:
            id=request.POST['bhayander_primary_hindi']
            obj=bhayander_primary_hindi.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_primary_hindi.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_primary'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['bhayander_primary_hindi_teacher']:
            id=request.POST['bhayander_primary_hindi_teacher']
            obj=bhayander_primary_hindi_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_primary_hindi_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_primary'))
    except Exception as e:
        print("type error: " + str(e))
    try:
        if request.POST['bhayander_secondary_english']:
            id=request.POST['bhayander_secondary_english']
            obj=bhayander_secondary_english.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_secondary_english.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_secondary'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['bhayander_secondary_english_teacher']:
            id=request.POST['bhayander_secondary_english_teacher']
            obj=bhayander_secondary_english_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_secondary_english_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_secondary'))
    except Exception as e:
        print("type error: " + str(e))
    try:
        if request.POST['bhayander_secondary_hindi']:
            id=request.POST['bhayander_secondary_hindi']
            obj=bhayander_secondary_hindi.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_secondary_hindi.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_secondary'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['bhayander_secondary_hindi_teacher']:
            id=request.POST['bhayander_secondary_hindi_teacher']
            obj=bhayander_secondary_hindi_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            bhayander_secondary_hindi_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('bhayander_admin_secondary'))
    except Exception as e:
        print("type error: " + str(e))
    
    
    return HttpResponseRedirect(reverse('bhayander_admin_index'))

def uplode_admin_bhayander(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    name=login_admin.objects.filter(username=username)
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    return render(request,'admin/add_admin_bhayander.html',{'name':name})

def save_admin_bhayander(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    path=request.POST['add']
    if path=='achive':
        name=request.POST['achive_name']
        achive=request.POST['achive_achive']
        discription=request.POST['achive_discription']
        image=''
        if request.method=='POST' and request.FILES['achive_image']:
            myfile=request.FILES['achive_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
             
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)

        s=bhayander_achivement(name=name,achive=achive,discription=discription,image=image,url=url)
        s.save()

    elif path=='event':
        branch=request.POST['bhayander_branch']
        name=request.POST['event_name']
        date=request.POST['event_date']
        time=request.POST['event_time']
        discription=request.POST['event_discription']
        image=''
        if request.method=='POST' and request.FILES['event_image']:
            myfile=request.FILES['event_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        if branch=='bhayander_event':
            s=bhayander_event(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_kinderGarten_english':
            s=bhayander_kinderGarten_english(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_kinderGarten_hindi':
            s=bhayander_kinderGarten_hindi(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_primary_english':
            s=bhayander_primary_english(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_primary_hindi':
            s=bhayander_primary_hindi(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_secondary_english':
            s=bhayander_secondary_english(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_secondary_hindi':
            s=bhayander_secondary_hindi(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_juniorCollege':
            s=bhayander_juniorCollege(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()

    elif path=='facility':
        name=request.POST['facility_name']
        discription=request.POST['facility_discription']
        image=''
        if request.method=='POST' and request.FILES['facility_image']:
            myfile=request.FILES['facility_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        s=bhayander_facility(name=name,discription=discription,image=image,url=url)
        s.save()
    elif path=='teachers':
        branch=request.POST['bhayander_teacher']
        name=request.POST['teacher_name']
        designation=request.POST['teacher_designation']
        discription=request.POST['teacher_discription']
        image=''
        if request.method=='POST' and request.FILES['teacher_image']:
            myfile=request.FILES['teacher_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        if branch=='bhayander_management':
            s=bhayander_management(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_kinderGarten_english_teacher':
            s=bhayander_kinderGarten_english_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_kinderGarten_hindi_teacher':
            s=bhayander_kinderGarten_hindi_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_primary_english_teacher':
            s=bhayander_primary_english_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_primary_hindi_teacher':
            s=bhayander_primary_hindi_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_secondary_english_teacher':
            s=bhayander_secondary_english_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_secondary_hindi_teacher':
            s=bhayander_secondary_hindi_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        elif branch=='bhayander_juniorCollege_teacher':
            s=bhayander_juniorCollege_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
    return HttpResponseRedirect(reverse('bhayander_admin_index'))

def nalasopara_admin_index(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))    
    name=login_admin.objects.filter(username=username)
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1 
    achive=nalasopara_achivement.objects.all()
    events=nalasopara_event.objects.all()
    facilities=nalasopara_facility.objects.all()
    managements=nalasopara_management.objects.all()
    return render(request,'admin/nalasopara_admin_index.html',{'achive':achive,'events':events,'facilities':facilities,'name':name,'managements':managements})

def nalasopara_admin_kinder_garten(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))    
    name=login_admin.objects.filter(username=username) 
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    obj=nalasopara_kinderGarten.objects.all()
    teacher=bhayander_juniorCollege_teacher.objects.all()
    return render(request,'admin/nalasopara_admin_kinder_garten.html',{'obj':obj,'name':name,'teacher':teacher})

def nalasopara_admin_primary(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))   
    name=login_admin.objects.filter(username=username) 
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    obj=nalasopara_primary_english.objects.all()
    obj1=nalasopara_primary_hindi.objects.all()
    teacher=nalasopara_primary_english_teacher.objects.all()
    teacher1=nalasopara_primary_hindi_teacher.objects.all()
    return render(request,'admin/nalasopara_admin_primary.html',{'obj':obj,'obj1':obj1,'name':name,'teacher':teacher,'teacher1':teacher1})

def nalasopara_admin_secondary(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))    
    name=login_admin.objects.filter(username=username) 
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    
    obj1=nalasopara_secondary_hindi.objects.all()
    
    teacher1=nalasopara_secondary_hindi_teacher.objects.all()
    return render(request,'admin/nalasopara_admin_secondary.html',{'obj1':obj1,'name':name,'teachers1':teacher1})

def delete_nalasopara(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    try:
        if request.POST['nalasopara_index_achivement']:
            id=request.POST['nalasopara_index_achivement']
            obj=nalasopara_achivement.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_achivement.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_index'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['nalasopara_index_event']:
            id=request.POST['nalasopara_index_event']
            obj=nalasopara_event.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_event.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_index'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['nalasopara_index_facility']:
            id=request.POST['nalasopara_index_facility']
            obj=nalasopara_facility.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_facility.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_index'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['nalasopara_index_management']:
            id=request.POST['nalasopara_index_management']
            obj=nalasopara_management.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_management.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_index'))
    except Exception as e:
        print("type error: " + str(e))
    try:
        if request.POST['nalasopara_kinder_garten']:
            id=request.POST['nalasopara_kinder_garten']
            obj=nalasopara_kinderGarten.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_kinderGarten.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_kinder_garten'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['nalasopara_kinder_garten_teacher']:
            id=request.POST['nalasopara_kinder_garten_teacher']
            obj=nalasopara_kinderGarten_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_kinderGarten_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_kinder_garten'))
    except Exception as e:
        print("type error: " + str(e))
    try:
        if request.POST['nalasopara_primary_english']:
            id=request.POST['nalasopara_primary_english']
            obj=nalasopara_primary_english.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_primary_english.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_primary'))
    except Exception as e:
        print("type error: " + str(e))
    
    try:
        if request.POST['nalasopara_primary_english_teacher']:
            id=request.POST['nalasopara_primary_english_teacher']
            obj=nalasopara_primary_english_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_primary_english_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_primary'))
    except Exception as e:
        print("type error: " + str(e))
    try:
        if request.POST['nalasopara_primary_hindi']:
            id=request.POST['nalasopara_primary_hindi']
            obj=nalasopara_primary_hindi.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_primary_hindi.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_primary'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['nalasopara_primary_hindi_teacher']:
            id=request.POST['nalasopara_primary_hindi_teacher']
            obj=nalasopara_primary_hindi_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_primary_hindi_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_primary'))
    except Exception as e:
        print("type error: " + str(e))
   
    try:
        if request.POST['nalasopara_secondary_hindi']:
            id=request.POST['nalasopara_secondary_hindi']
            obj=nalasopara_secondary_hindi.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_secondary_hindi.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_secondary'))
    except Exception as e:
        print("type error: " + str(e))
    
    try:
        if request.POST['nalasopara_secondary_hindi_teacher']:
            id=request.POST['nalasopara_secondary_hindi_teacher']
            obj=nalasopara_secondary_hindi_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            nalasopara_secondary_hindi_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('nalasopara_admin_secondary'))
    except Exception as e:
        print("type error: " + str(e))
    return HttpResponseRedirect(reverse('nalasopara_admin_index'))
        
def uplode_admin_nalasopara(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    name=login_admin.objects.filter(username=username)
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    return render(request,'admin/add_admin_nalasopara.html',{'name':name})

def save_admin_nalasopara(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    path=request.POST['add']
    if path=='achive':
        name=request.POST['achive_name']
        achive=request.POST['achive_achive']
        discription=request.POST['achive_discription']
        image=''
        if request.method=='POST' and request.FILES['achive_image']:
            myfile=request.FILES['achive_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        s=nalasopara_achivement(name=name,achive=achive,discription=discription,image=image,url=url)
        s.save()

    elif path=='event':
        branch=request.POST['nalasopara_branch']
        name=request.POST['event_name']
        date=request.POST['event_date']
        time=request.POST['event_time']
        discription=request.POST['event_discription']
        image=''
        if request.method=='POST' and request.FILES['event_image']:
            myfile=request.FILES['event_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        if branch=='nalasopara_event':
            s=nalasopara_event(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
        elif branch=='nalasopara_kinderGarten':
            s=nalasopara_kinderGarten(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
    
        elif branch=='nalasopara_primary_english':
            s=nalasopara_primary_english(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
        elif branch=='nalasopara_primary_hindi':
            s=nalasopara_primary_hindi(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
        
        elif branch=='nalasopara_secondary_hindi':
            s=nalasopara_secondary_hindi(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()

    elif path=='facility':
        name=request.POST['facility_name']
        discription=request.POST['facility_discription']
        image=''
        if request.method=='POST' and request.FILES['facility_image']:
            myfile=request.FILES['facility_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        s=nalasopara_facility(name=name,discription=discription,image=image,url=url)
        s.save()
    elif path=='teachers':
        branch=request.POST['nalasopara_teacher']
        name=request.POST['teacher_name']
        designation=request.POST['teacher_designation']
        discription=request.POST['teacher_discription']
        image=''
        if request.method=='POST' and request.FILES['teacher_image']:
            myfile=request.FILES['teacher_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        if branch=='nalasopara_management':
            s=nalasopara_management(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        elif branch=='nalasopara_kinderGarten_teacher':
            s=nalasopara_kinderGarten_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        elif branch=='nalasopara_primary_english_teacher':
            s=nalasopara_primary_english_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        elif branch=='nalasopara_primary_hindi_teacher':
            s=nalasopara_primary_hindi_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        elif branch=='nalasopara_secondary_hindi_teacher':
            s=nalasopara_secondary_hindi_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
    return HttpResponseRedirect(reverse('nalasopara_admin_index'))


def virar_admin_index(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))   
    name=login_admin.objects.filter(username=username) 
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    achive=virar_achivement.objects.all()
    events=virar_event.objects.all()
    facilities=virar_facility.objects.all()
    managements=virar_management.objects.all()
    return render(request,'admin/virar_admin_index.html',{'achive':achive,'events':events,'facilities':facilities,'name':name,'managements':managements})

def virar_admin_primary(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))    
    name=login_admin.objects.filter(username=username) 
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    
    obj1=virar_primary_hindi.objects.all()
    teacher=virar_primary_hindi_teacher.objects.all()
    return render(request,'admin/virar_admin_primary.html',{'obj1':obj1,'name':name,'teacher':teacher})

def virar_admin_secondary(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))  
    name=login_admin.objects.filter(username=username) 
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    
    obj1=virar_secondary_hindi.objects.all()
    teacher=virar_secondary_hindi_teacher.objects.all()
    return render(request,'admin/virar_admin_secondary.html',{'obj1':obj1,'name':name,'teacher':teacher})

def delete_virar(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    try:
        if request.POST['virar_index_achivement']:
            id=request.POST['virar_index_achivement']
            obj=virar_achivement.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            virar_achivement.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('virar_admin_index'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['virar_index_event']:
            id=request.POST['virar_index_event']
            obj=virar_event.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            virar_event.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('virar_admin_index'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['virar_index_facility']:
            id=request.POST['virar_index_facility']
            obj=virar_facility.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            virar_facility.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('virar_admin_index'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['virar_index_management']:
            id=request.POST['virar_index_management']
            obj=virar_management.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            virar_management.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('virar_admin_index'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['virar_primary_hindi']:
            id=request.POST['virar_primary_hindi']
            obj=virar_primary_hindi.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            virar_primary_hindi.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('virar_admin_primary'))
    except Exception as e:
        print("type error: " + str(e))

    try:
        if request.POST['virar_primary_teacher']:
            id=request.POST['virar_primary_teacher']
            obj=virar_primary_hindi_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            virar_primary_hindi_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('virar_admin_primary'))
    except Exception as e:
        print("type error: " + str(e))   

    try:
        if request.POST['virar_secondary_hindi']:
            id=request.POST['virar_secondary_hindi']
            obj=virar_secondary_hindi.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            virar_secondary_hindi.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('virar_admin_secondary'))
    except Exception as e:
        print("type error: " + str(e))
    
    try:
        if request.POST['virar_secondary_teacher']:
            id=request.POST['virar_secondary_teacher']
            obj=virar_secondary_hindi_teacher.objects.filter(id=id)
            for i in obj:
                path=i.url
                print(path)
            path=str(path)
            if os.path.isfile(path):
                os.remove(path)
            virar_secondary_hindi_teacher.objects.filter(id=id).delete()
            return HttpResponseRedirect(reverse('virar_admin_secondary'))
    except Exception as e:
        print("type error: " + str(e))
    
    return HttpResponseRedirect(reverse('virar_admin_index'))


def uplode_admin_virar(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    name=login_admin.objects.filter(username=username)
    for i in name:
        user=i.first_name
        user1=i.last_name
    name=' '+user+' '+user1
    return render(request,'admin/add_admin_virar.html',{'name':name})

def save_admin_virar(request):
    try:
        username=request.session['username']
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))
    path=request.POST['add']
    if path=='achive':
        name=request.POST['achive_name']
        achive=request.POST['achive_achive']
        discription=request.POST['achive_discription']
        image=''
        if request.method=='POST' and request.FILES['achive_image']:
            myfile=request.FILES['achive_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        s=virar_achivement(name=name,achive=achive,discription=discription,image=image,url=url)
        s.save()

    elif path=='event':
        branch=request.POST['virar_branch']
        name=request.POST['event_name']
        date=request.POST['event_date']
        time=request.POST['event_time']
        discription=request.POST['event_discription']
        image=''
        if request.method=='POST' and request.FILES['event_image']:
            myfile=request.FILES['event_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        if branch=='virar_event':
            s=virar_event(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
         
        elif branch=='virar_primary_hindi':
            s=virar_primary_hindi(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()
        
        elif branch=='virar_secondary_hindi':
            s=virar_secondary_hindi(name=name,date=date,time=time,discription=discription,image=image,url=url)
            s.save()

    elif path=='facility':
        name=request.POST['facility_name']
        discription=request.POST['facility_discription']
        image=''
        if request.method=='POST' and request.FILES['facility_image']:
            myfile=request.FILES['facility_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        s=virar_facility(name=name,discription=discription,image=image,url=url)
        s.save()
    elif path=='teachers':
        branch=request.POST['virar_teacher']
        name=request.POST['teacher_name']
        designation=request.POST['teacher_designation']
        discription=request.POST['teacher_discription']
        image=''
        if request.method=='POST' and request.FILES['teacher_image']:
            myfile=request.FILES['teacher_image']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            image=fs.url(filename)
            name_img=image[7:]
            url=str(MEDIA_ROOT)+'/'+str(name_img)
            img=Image.open(url)
            img1=copy.deepcopy(img)
            img.close()
            os.remove(url)
            img1=img1.resize((455,460))
            img1.save(url)
        if branch=='virar_management':
            s=virar_management(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        
        elif branch=='virar_primary_teacher':
            s=virar_primary_hindi_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
        
        elif branch=='virar_secondary_teacher':
            s=virar_secondary_hindi_teacher(name=name,designation=designation,discription=discription,image=image,url=url)
            s.save()
       

    return HttpResponseRedirect(reverse('virar_admin_index'))
