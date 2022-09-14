from django.shortcuts import render, HttpResponse, redirect
from tuitionapplication.models import Finaltutorprofile, Finalstudentprofile, Finalstudentregister
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string
from tuitionsoftware.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER

# Create your views here.
#######################################################################################
#######################################################################################
#######################################################################################

##############TUTION MANAGEMENT SYSTEM#############


def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')



def handleSignup(request): 
    
    if request.method=='GET':
        return render(request, 'signup.html')
    if request.method=='POST':
        #Get parameters posted
        username=request.POST['username']
        userid=request.POST['userid']
        emailsignup=request.POST['emailsignup']
        firstnamesignup=request.POST['firstnamesignup']
        lastnamesignup=request.POST['lastnamesignup']  
        phonesignup=request.POST['phonesignup']
        passsignup=request.POST['passsignup']
        

        myuser = User.objects.create_user(username, emailsignup, passsignup)
        myuser.user_id=userid
        #myuser.Last_name=Slastname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        #finalprofiletutorder = Finaltutorprofile.objects.filter(userid=lk)
        #print(finalprofiletutorder)
        

        tosign = request.POST.get('emailsignup')
        print(tosign)
        send_mail(
            'You have signed in successfully.',
            'Go Back to the website to Login.',
            settings.EMAIL_HOST_USER,
            [tosign]
        )
        
        return redirect('/')
        #return render(request, '/', {"finalprofiletutorder":finalprofiletutorder})

def handleLogin(request):
    if request.method=='GET':
        return render(request, 'login.html')
        
    if request.method=='POST':
        usernamelogin=request.POST['usernamelogin'] 
        passlogin=request.POST['passlogin']

        user=authenticate(username=usernamelogin, password=passlogin) #signup
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('handleLogin')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')


def tutcreateprofile(request):
    finalprofiletutorder = Finaltutorprofile.objects.all()
    #finalprofiletutorder = Finaltutorprofile.objects.get(pk=1)
    
   
   
    if request.method=="POST":
        idtutor=request.POST['idtutor']
        inputfirstnamet=request.POST['inputfirstnamet']
        inputlastnamet=request.POST['inputlastnamet']
        inputemailt=request.POST['inputemailt']
        inputphonet=request.POST['inputphonet']
        inputtypet=request.POST['inputtypet']
        inputaddresst=request.POST['inputaddresst']
        inputpict=request.POST['inputpict']
        inputcoursest=request.POST['inputcoursest']
        inputexperiencet=request.POST['inputexperiencet']
        inputaget=request.POST['inputaget']
        inputorgt=request.POST['inputorgt']
        inputtimet=request.POST['inputtimet']
        inputseatt=request.POST['inputseatt']
        inputmodet=request.POST['inputmodet']
        
        finaltutprofiledata = Finaltutorprofile(idtutor=idtutor, inputfirstnamet=inputfirstnamet, inputlastnamet=inputlastnamet, inputemailt=inputemailt, inputphonet=inputphonet, inputtypet=inputtypet, inputaddresst=inputaddresst, inputpict=inputpict, inputcoursest=inputcoursest, inputexperiencet=inputexperiencet, inputaget=inputaget, inputorgt=inputorgt, inputtimet=inputtimet, inputseatt=inputseatt, inputmodet=inputmodet)  

        finaltutprofiledata.save()
        messages.success(request, "Tutor Profile succesfully created and saved")
        finalprofiletutorder = Finaltutorprofile.objects.filter(pk=idtutor)
        print(finalprofiletutorder)
        return redirect('tutorprofileview', pk=finaltutprofiledata.idtutor)
    return render(request,"tutcreateprofile.html",{"Ftutprofileorders":finalprofiletutorder})
        
    #return redirect('tutorprofileview', pk=finalprofiletutorder.idtutor, {"Ftutprofileorders":finalprofiletutorder})
    #return redirect('tutorprofileview', pk=finalprofiletutorder.idtutor)

def tutorprofileview(request, pk):
    finalprofiletutorder = Finaltutorprofile.objects.filter(idtutor=pk)
    print(finalprofiletutorder)
    
    return render(request, 'tutorprofileview.html', {"finalprofiletutorder":finalprofiletutorder})
    #return redirect('tutorprofile', pk=finalprofiletutorder.idtutor)


def tutorlist(request):
    #num1=Finalstudentprofile.objects.count()
    finalprofiletutorder = Finaltutorprofile.objects.all()
    print(finalprofiletutorder)
    return render(request, 'tutorlist.html', {"finalprofiletutorder":finalprofiletutorder})
    #return HttpResponse("This is my home page")
    #return render(request, 'tutorprofile.html')
    

def tutorprofile(request, pk):
    finalprofiletutorder = Finaltutorprofile.objects.filter(idtutor=pk)
    print(finalprofiletutorder)
    return render(request, 'tutorprofile.html', {"finalprofiletutorder":finalprofiletutorder})
    #return HttpResponse("This is my home page")
    #return render(request, 'tutorprofile.html')

def tutordashboard(request, pk):
    #return HttpResponse("This is my home page")
    #return render(request, 'tutordashboard.html')
    finalprofiletutorder = Finaltutorprofile.objects.filter(idtutor=pk)
    finalregisterstudorder = Finalstudentregister.objects.filter(tutoridnew=pk)
    print(finalprofiletutorder, finalregisterstudorder)
    return render(request, 'tutordashboard.html', {"finalprofiletutorder":finalprofiletutorder, "finalregisterstudorder":finalregisterstudorder})

def studcreateprofile(request):
    finalprofilestudorder = Finalstudentprofile.objects.all()
    if request.method=="POST":
        idstudent=request.POST['idstudent']
        inputfirstnamestu=request.POST['inputfirstnamestu']
        inputlastnamestu=request.POST['inputlastnamestu']
        inputemailstu=request.POST['inputemailstu']
        inputphonestu=request.POST['inputphonestu']
        inputtypestu=request.POST['inputtypestu']
        inputaddressstu=request.POST['inputaddressstu']
        inputclassstu=request.POST['inputclassstu']
        inputbranchstu=request.POST['inputbranchstu']
        inputexperiencestu=request.POST['inputexperiencestu']
        inputagestu=request.POST['inputagestu']
        inputgenstu=request.POST['inputgenstu']
        inputtimestu=request.POST['inputtimestu']
        inputmodestu=request.POST['inputmodestu']
        
        finalstudprofiledata = Finalstudentprofile(idstudent=idstudent, inputfirstnamestu=inputfirstnamestu, inputlastnamestu=inputlastnamestu, inputemailstu=inputemailstu, inputphonestu=inputphonestu, inputtypestu=inputtypestu, inputaddressstu=inputaddressstu, inputclassstu=inputclassstu, inputbranchstu=inputbranchstu, inputexperiencestu=inputexperiencestu, inputagestu=inputagestu, inputgenstu=inputgenstu, inputtimestu=inputtimestu, inputmodestu=inputmodestu)  

        finalstudprofiledata.save()
        messages.success(request, "Student Profile succesfully created and saved")
        #finalprofilestudorder = Finalstudentprofile.objects.filter(ik=idstudent)
        #print(finalprofilestudorder)
        #return redirect('studentprofileview', ik=finalstudprofiledata.idstudent)
              
    #return render(request,"studcreateprofile.html",{"Fstudprofileorders":finalprofilestudorder})
    return render(request,"studcreateprofile.html",{"Fstudprofileorders":finalprofilestudorder})

def studentprofileview(request, ik):
    finalprofilestudorder = Finalstudentprofile.objects.filter(idstudent=ik)
    print(finalprofilestudorder)
    
    return render(request, 'studentprofileview.html', {"finalprofilestudorder":finalprofilestudorder})
    #return redirect('tutorprofile', pk=finalprofiletutorder.idtutor)


def studentlist(request):
    #num1=Finalstudentprofile.objects.count()
    finalprofilestudorder = Finalstudentprofile.objects.all()
    print(finalprofilestudorder)
    return render(request, 'studentlist.html', {"finalprofilestudorder":finalprofilestudorder})
    #return HttpResponse("This is my home page")
    #return render(request, 'tutorprofile.html')
    
    
def studentprofile(request, ik):
    #num1=Finalstudentprofile.objects.count()
    finalprofilestudorder = Finalstudentprofile.objects.filter(idstudent=ik)
    print(finalprofilestudorder)
               
    return render(request, 'studentprofile.html', {"finalprofilestudorder":finalprofilestudorder})
    #return HttpResponse("This is my home page")
    #return render(request, 'tutorprofile.html')
    

def studentdashboardpage(request, ik): #take from registeration
    #return HttpResponse("This is my home page")
    #return render(request, 'studentdashboardpage.html')
    #finalprofiletutorder = Finaltutorprofile.objects.all()
    #finalprofilestudorder = Finalstudentprofile.objects.filter(idstudent=ik)
    finalprofilestudorder = Finalstudentprofile.objects.filter(idstudent=ik)
    finalregisterstudorder = Finalstudentregister.objects.filter(registernewid=ik)
    print(finalprofilestudorder, finalregisterstudorder)
    return render(request, 'studentdashboardpage.html', {"finalprofilestudorder":finalprofilestudorder, "finalregisterstudorder":finalregisterstudorder})

def registernewcourse(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'registernewcourse.html')
    finalregisterstudorder = Finalstudentregister.objects.all()
    if request.method=="POST":
        registernewid=request.POST['registernewid']
        registernewcontact=request.POST['registernewcontact']
        registernewemail=request.POST['registernewemail']
        studentnotetotutor=request.POST['studentnotetotutor']
        tutoridnew=request.POST['tutoridnew']
        tutornewemail=request.POST['tutornewemail']
        coursesregistered=request.POST['coursesregistered']
        
        finalstudregisterdata = Finalstudentregister(registernewid=registernewid, registernewcontact=registernewcontact, registernewemail=registernewemail, studentnotetotutor=studentnotetotutor, tutoridnew=tutoridnew, tutornewemail=tutornewemail, coursesregistered=coursesregistered)  

        finalstudregisterdata.save()
        messages.success(request, "Course Registered Successfully") 
        
        tosign = request.POST.get('tutornewemail')
        conver = request.POST.get('registernewid')
        conver1 = request.POST.get('registernewcontact')
        conver2 = request.POST.get('registernewemail')
        conver3 = request.POST.get('studentnotetotutor')
        conver4 = request.POST.get('coursesregistered')
        print(tosign)
        send_mail(
            'A New Registration Recieved.',
            'Student ID '+ conver +' has Registered. Courses: ' + conver4+ ' Phone Number: '+ conver1 + ' Email ID: ' + conver2 + ' Note: ' + conver3,
            settings.EMAIL_HOST_USER,
            [tosign]
        )
        
        
                     
    return render(request,"registernewcourse.html",{"Fstudregisterorders":finalregisterstudorder})

def searchpage(request):
    finalprofiletutorder = Finaltutorprofile.objects.all()
    print(finalprofiletutorder)
    return render(request, 'searchpage.html', {"finalprofiletutorder":finalprofiletutorder})



def editprofilestudent(request):
    #return HttpResponse("This is my home page")
    return render(request, 'editprofilestudent.html')

def editprofiletutor(request):
    #return HttpResponse("This is my home page")
    return render(request, 'editprofiletutor.html')



