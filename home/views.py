from django.shortcuts import render, HttpResponse,redirect
from django.db import connection,transaction,IntegrityError
from .models import R21,R22
import requests
from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .scrap import forcesrate, coderate, leetrate, spojrate,get

# Create your views here.



def index(request):
    return render(request, 'index.html')

def admin_panel(request):
    return render(request,'admin_panel1.html')

def display_students(request, year, br):
    global students    
    if (year == '3rd'):
        if (br != 'all'):
            students = R21.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R21.objects.all().order_by('-overall_score')
        
    if (year == '2nd'):
        if (br != 'all'):
            
            students = R22.objects.all().order_by('-overall_score').filter(branch=br)
            print("hello")
            print(students)
            return students
        
        students = R22.objects.all().order_by('-overall_score')
        
    if (year == '1st'):
        if (br != 'all'):
            students = R23.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R23.objects.all().order_by('-overall_score')

    if (year == '4th'):
        if (br != 'all'):
            students = R20.objects.all().order_by('-overall_score').filter(branch=br)
            return students

        students = R20.objects.all().order_by('-overall_score')

    return students
    # return render(request,'display.html',context)

 
    


def validate(request):
    if request.method == 'POST':
        details = request.POST.dict()
        year = details['year']
        branch = details['branch']
        print(year, branch)

        students = display_students(request, year, branch)
        
        context = {
            'students': students
            
        }
        return render(request, 'over_view.html', context)

def report(request):
    context = {
            'students': students
            
        }
    return render(request,'report.html',context)
def update(request):

    students = R21.objects.all().values()

    cc_ids = {}
    cf_ids = {}
    sp_ids={}
    cc_res = {}
    cf_res = {}
    sp_res={}
    c = 0
    for i in students:
        cc_ids.update({i['codechef_username']: 0})
        cf_ids.update({i['codeforces_username']: 0})
        if(i['spoj_username']=='deep nandan'):
            continue
        sp_ids.update({i['spoj_username']: 0})

    #     c = c + 1
    #    # c IS FOR TESTING PURPOSE ONLY
    #     if (c > 30):
    #         break

    cc_res.update(get(cc_ids, coderate))
    cf_res.update(get(cf_ids, forcesrate))
    sp_res.update(get(sp_ids, spojrate))

    print(sp_res)

    
    try:
        with transaction.atomic():
            for key, value in cc_res.items():
                R21.objects.filter(codechef_username=key).update(cc_problems_solved=value)
                R21.objects.filter(codechef_username=key).update(ccps_10=value*10)
            for key,value in cf_res.items():
                 R21.objects.filter(codeforces_username=key).update(cf_problems_solved=value)
                 R21.objects.filter(codeforces_username=key).update(cfps_10=value*10)
            for key,value in sp_res.items():
                R21.objects.filter(codeforces_username=key).update(cf_problems_solved=value)
                R21.objects.filter(codeforces_username=key).update(sps_20=value*20)
            
        with connection.cursor() as cursor:
            cursor.callproc('update_overall_score')
            cursor.callproc('update_rank')
            cursor.close()             

    except IntegrityError:
        return HttpResponse("DB ERROR")
    

    return HttpResponse("updated")
    
def auth_login(request):
    if request.GET.get('next'):
        messages.add_message(request, messages.WARNING,
                             "Please login before proceeding")

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)
            if user.is_superuser:
                return redirect("/admin_panel")
            return redirect("/profile")
        else:
            return HttpResponse("Enter correct credentials")
    return render(request, 'login.html')


def auth_logout(request):
     logout(request)
     return redirect("/login")

@login_required(login_url='/login')
def profile(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "profile.html", {'username': username})
