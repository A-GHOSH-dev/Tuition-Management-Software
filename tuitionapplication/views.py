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
        emailsignup=request.POST['emailsignup']
        firstnamesignup=request.POST['firstnamesignup']
        lastnamesignup=request.POST['lastnamesignup']  
        phonesignup=request.POST['phonesignup']
        passsignup=request.POST['passsignup']
        

        myuser = User.objects.create_user(username, emailsignup, passsignup)
        myuser.person_name=firstnamesignup
        #myuser.Last_name=Slastname
        myuser.save()
        messages.success(request, "Your account has been successfully created")

        '''tosign = request.POST.get('emailsignup')
        print(tosign)
        send_mail(
            'You have signed in successfully.',
            'Go Back to the website to Login.',
            settings.EMAIL_HOST_USER,
            [tosign]
        )'''
        
        return redirect('/')

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
              
    return render(request,"tutcreateprofile.html",{"Ftutprofileorders":finalprofiletutorder})

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
    print(finalprofiletutorder)
    return render(request, 'tutordashboard.html', {"finalprofiletutorder":finalprofiletutorder})

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
              
    #return render(request,"studcreateprofile.html",{"Fstudprofileorders":finalprofilestudorder})
    return render(request,"studcreateprofile.html",{"Fstudprofileorders":finalprofilestudorder})

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
    finalprofiletutorder = Finaltutorprofile.objects.all()
    finalprofilestudorder = Finalstudentprofile.objects.filter(idstudent=ik)
    print(finalprofilestudorder, finalprofiletutorder)
    return render(request, 'studentdashboardpage.html', {"finalprofilestudorder":finalprofilestudorder, "finalprofiletutorder":finalprofiletutorder})

def registernewcourse(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'registernewcourse.html')
    finalregisterstudorder = Finalstudentregister.objects.all()
    if request.method=="POST":
        
        registernewcontact=request.POST['registernewcontact']
        registernewemail=request.POST['registernewemail']
        studentnotetotutor=request.POST['studentnotetotutor']
        tutorprofilelink=request.POST['tutorprofilelink']
        coursesregistered=request.POST['coursesregistered']
        
        finalstudregisterdata = Finalstudentregister(registernewcontact=registernewcontact, registernewemail=registernewemail, studentnotetotutor=studentnotetotutor, tutorprofilelink=tutorprofilelink, coursesregistered=coursesregistered)  

        finalstudregisterdata.save()
        messages.success(request, "Course Registered Successfully")
              
    return render(request,"registernewcourse.html",{"Fstudregisterorders":finalregisterstudorder})



def editprofilestudent(request):
    #return HttpResponse("This is my home page")
    return render(request, 'editprofilestudent.html')

def editprofiletutor(request):
    #return HttpResponse("This is my home page")
    return render(request, 'editprofiletutor.html')



