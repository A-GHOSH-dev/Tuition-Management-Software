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
def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')

def dashboard(request):
    finalreportorder = Finalreport.objects.all()

    #return HttpResponse("This is my home page")
    return render(request, 'dashboard.html', {'finalreportorder':finalreportorder})

def allincidentslist(request):
    incidentreportingorder = Incidentreporting.objects.all()
    assigninvestigatororder = Assigninvestigator.objects.all()
    
    #return HttpResponse("This is my home page")
    #return render(request, 'allincidentslist.html')
    return render(request,"allincidentslist.html",{"incidentreportingorder":incidentreportingorder, "assigninvestigatororder":assigninvestigatororder })
def incidentenquiry(request):
    incidentreportingorder = Incidentreporting.objects.all()
    finalreportorder = Finalreport.objects.all()
    verifyactionorder = Verifyactionclose.objects.all()
    return render(request,"incidentenquiry.html",{"incidentreportingorder":incidentreportingorder, "finalreportorder":finalreportorder, "verifyactionorder":verifyactionorder})
    #return HttpResponse("This is my home page")
    #return render(request, 'incidentenquiry.html') 

def handleSignup(request): #adduser
    if request.method=='GET':
        return render(request, 'signup.html')
    if request.method=='POST':
        #Get parameters posted
        username=request.POST['emp_id']
        email=request.POST['email']
        name=request.POST['name']  
        Department=request.POST['Department']
        FactoryNumber=request.POST['FactoryNumber']
        first_name=request.POST['role_of_user']
        user_designation=request.POST['user_designation']
        phone=request.POST['phone']
        user_training=request.POST['user_training']
        password1=request.POST['password1']
        password2=request.POST['password2']

        myuser = User.objects.create_user(username, email, password1)
        myuser.person_name=first_name
        myuser.save()
        messages.success(request, "Your account has been successfully created")

        tosign = request.POST.get('email')
        contentsign = request.POST.get('emp_id')
        password1sign = request.POST.get('password1')
        role_of_usersign=request.POST.get('role_of_user')
        print(tosign, contentsign)
        send_mail(
            'You have been added',
            'EMPLOYEE ID: ' + contentsign +'.' + ' PASSWORD: ' + password1sign + '.' + ' ROLE: '+role_of_usersign +'.',
            settings.EMAIL_HOST_USER,
            [tosign]
        )
        
        return redirect('/')

def handleLogin(request):
    if request.method=='GET':
        return render(request, 'login.html')
        
    if request.method=='POST':
        loginemp_id=request.POST['loginemp_id'] 
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginemp_id, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('handleLogin')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')

'''def profilepage(request):
    if request.user.is_authenticated:
        emp_id=request.user.emp_id
        email=request.user.email
        name=request.user.name
        Department=request.user.Departmente
        FactoryNumber=request.user.FactoryNumber
        role_of_user=request.user.role_of_user
        user_designation=request.user.user_designation
        phone=request.user.phone
        user_training=request.user.user_training
        password1=request.user.password1
        return render(request, 'profilepage.html')
    else:
        return redirect('handleLogin')

    #return render(request, 'profilepage.html')'''


def profilepage(request):
    adduserorder = Adduser.objects.all()
    return render(request,"profilepage.html",{"adduserorder":adduserorder})

def adduser(request):#createprofile
    adduserorder = Adduser.objects.all()
    #return HttpResponse("This is my home page")
    #return render(request, 'adduser.html')
    if request.method=="POST":

        addemp_id=request.POST['addemp_id']
        addemail=request.POST['addemail']
        addname=request.POST['addname']
        adddepartment=request.POST['adddepartment']
        addsection=request.POST['addsection']
        designation=request.POST['designation']
        addrole=request.POST['addrole']
        addtraining=request.POST['addtraining']
        addphone=request.POST['addphone']
        addpassword=request.POST['addpassword']

        adduserdata = Adduser(addemp_id=addemp_id, addemail=addemail, addname=addname, adddepartment=adddepartment, addsection=addsection, designation=designation, addrole=addrole, addtraining=addtraining, addphone=addphone, addpassword=addpassword)  

        adduserdata.save()
        
        messages.success(request, "User Profile has been succesfully created")

        return redirect('profilepage')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    #return render(request,"adduser.html")
    return render(request,"adduser.html",{"Us":adduserorder})

def incidentreport(request):
    incidentreportingorder = Incidentreporting.objects.all()
    #return HttpResponse("This is my home page")
    #return render(request, 'incidentreport.html')
    if request.method=="POST":
        reportingincident_id=request.POST['reportingincident_id']
        datereport=request.POST['datereport']
        timereport=request.POST['timereport']
        reportedby=request.POST['reportedby']
        dateincident=request.POST['dateincident'] #this
        timeincident=request.POST['timeincident']
        locationincident=request.POST['locationincident'] #this
        incidentdesc=request.POST['incidentdesc']
        incidentaction=request.POST['incidentaction']
        victimname=request.POST['victimname']
        victimrole=request.POST['victimrole']
        victimemp_id=request.POST['victimemp_id']
        victimcon_id=request.POST['victimcon_id']
        assign_inv_email=request.POST['assign_inv_email']

        incidentreportingdata = Incidentreporting(reportingincident_id=reportingincident_id, datereport=datereport, timereport=timereport, reportedby=reportedby, dateincident=dateincident, timeincident=timeincident, locationincident=locationincident, incidentdesc=incidentdesc, incidentaction=incidentaction, victimname=victimname, victimrole=victimrole, victimemp_id=victimemp_id, victimcon_id=victimcon_id, assign_inv_email=assign_inv_email)  

        incidentreportingdata.save()
        messages.success(request, "Incident has been succesfully reported")

        to = request.POST.get('assign_inv_email')
        content = request.POST.get('reportingincident_id')
        print(to, content)
        send_mail(
            'Incient Reported',
            content +' has been reported',
            settings.EMAIL_HOST_USER,
            [to]
        )
        return render(
            request,
            'incidentreport.html',
            {
                'title':'send an email'
            }
        )
        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    #return render(request,"incidentreport.html")
    return render(request,"incidentreport.html",{"Orders":incidentreportingorder, "incidentreportingorder":incidentreportingorder})

def assignleadinvestigator(request):
    assigninvestigatororder = Assigninvestigator.objects.all()
    #return HttpResponse("This is my home page")
    #return render(request, 'assignleadinvestigator.html')
    if request.method=="POST":
        incident_id=request.POST['incident_id']
        nameassignedinvestigator=request.POST['nameassignedinvestigator']
        emailassignedinvestigator=request.POST['emailassignedinvestigator']

        assignleadinvestigatorreport = Assigninvestigator(incident_id=incident_id, nameassignedinvestigator=nameassignedinvestigator, emailassignedinvestigator=emailassignedinvestigator)  

        assignleadinvestigatorreport.save()
        messages.success(request, "Lead investigator has been succesfully assigned")
        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        toinv = request.POST.get('emailassignedinvestigator')
        contentinv = request.POST.get('incident_id')
        print(toinv, contentinv)
        send_mail(
            'Incident Reported',
            'Incident with ID '+ contentinv +' has been assigned to you',
            settings.EMAIL_HOST_USER,
            [toinv]
        )
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    #return render(request,"assignleadinvestigator.html")
    return render(request,"assignleadinvestigator.html",{"Aincident":assigninvestigatororder})

def whywhyanalysis(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'whywhyanalysis.html')
    if request.method=="POST":
        whyinc_id=request.POST['whyinc_id']
        ps=request.POST['ps']
        why1=request.POST['why1']
        why2=request.POST['why2']
        why3=request.POST['why3']
        why4=request.POST['why4']
        why5=request.POST['why5']
        rc=request.POST['rc']

        whywhyanalysisdata = Whywhyanalyzing(whyinc_id=whyinc_id, ps=ps, why1=why1, why2=why2, why3=why3, why4=why4, why5=why5, rc=rc)  

        whywhyanalysisdata.save()
        messages.success(request, "Why Why Analysis Done")

    
        return redirect('specialanalysis')
        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    return render(request,"whywhyanalysis.html")

def specialanalysis(request):
    if request.method=="POST":
        spe_inc_id =request.POST['spe_inc_id']
        imm_cause_unsafe_ac = request.POST['imm_cause_unsafe_ac']
        imm_cause_unsafe_con = request.POST['imm_cause_unsafe_con']
        root_cause_human_fac = request.POST['root_cause_human_fac']
        root_cause_org_fac = request.POST['root_cause_org_fac']

        specialanalysisdata = Specialanalyzing(spe_inc_id=spe_inc_id, imm_cause_unsafe_ac=imm_cause_unsafe_ac, imm_cause_unsafe_con=imm_cause_unsafe_con, root_cause_human_fac=root_cause_human_fac, root_cause_org_fac=root_cause_org_fac)  

        specialanalysisdata.save()
        messages.success(request, "Special Analysis Done")

    
        return redirect('finalinvestigationreport')

    return render(request,"specialanalysis.html")
'''
def specialanalysis(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'whywhyanalysis.html')
    if request.method=="POST":
        speinc_id=request.POST['speinc_id']
        speicua = request.POST.getlist('icua[]')
        data_icua=''
        if(len(speicua)>0):
          for data_icua1 in speicua:
            data_icua=data_icua+data_icua1 +" " 
        icuao=request.POST['icuao']
        speicuc = request.POST.getlist('icuc[]')
        data_icuc=''
        if(len(speicua)>0):
          for data_icuc1 in speicua:
            data_icuc=data_icuc+data_icuc1 +" " 
        icuco=request.POST['icuco']
        sperchf = request.POST.getlist('rchf[]')
        data_rchf=''
        if(len(sperchf)>0):
          for data_rchf1 in sperchf:
            data_rchf=data_rchf+data_rchf1 +" "  
        rchfo=request.POST['rchfo'] 
        spercof = request.POST.getlist('rcof[]')
        data_rcof=''
        if(len(spercof)>0):
          for data_rcof1 in spercof:
            data_rcof=data_rcof+data_rcof1 +" " 
        rcofo=request.POST['rcofo']  

        specialanalysisdata = SpecialAnalyzing(speinc_id=speinc_id, speicua=speicua, speicuc=speicuc, sperchf=sperchf, spercof=spercof, icuao=icuao, icuco=icuco, rchfo=rchfo, rcofo=rcofo)  

        specialanalysisdata.save()
        messages.success(request, "Special Analysis Done")

    
        return redirect('finalinvestigationreport')
        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    return render(request,"specialanalysis.html")

'''
def finalinvestigationreport(request):
    finalreportorder = Finalreport.objects.all()
    #return HttpResponse("This is my home page")
    #return render(request, 'whywhyanalysis.html')
    if request.method=="POST":
        reinc_id=request.POST['reinc_id'] #this
        reinc_type=request.POST['reinc_type'] #this
        summary=request.POST['summary']
        inv_name = request.POST['inv_name']
        inv_id = request.POST['inv_id']
        re_date = request.POST['re_date']
        re_time = request.POST['re_time']
        re_loc = request.POST['re_loc']
        inv_vic_name = request.POST['inv_vic_name']
        injuries = request.POST['injuries']
        fatalities = request.POST['fatalities']
        vic_fat_desc = request.POST['vic_fat_desc']
        #img=request.POST['img']
        rca=request.POST['rca']
        imc=request.POST['imc']
        rtc=request.POST['rtc']
        ca=request.POST['ca']
        cap=request.POST['cap']
        cad=request.POST['cad']
        pa=request.POST['pa']
        pap=request.POST['pap']
        pat=request.POST['pat']
        ma=request.POST['ma']
        intensity = request.POST['intensity'] #this

        finalinvestigationreportdata = Finalreport(reinc_id=reinc_id, reinc_type=reinc_type, summary=summary, rca=rca, imc=imc, rtc=rtc, ca=ca, cap=cap, cad=cad, pa=pa, pap=pap, pat=pat, intensity=intensity, vic_fat_desc=vic_fat_desc, fatalities=fatalities, injuries=injuries, inv_vic_name=inv_vic_name, inv_name=inv_name, inv_id=inv_id, re_date=re_date, re_time=re_time, re_loc=re_loc, ma=ma)  

        finalinvestigationreportdata.save()
        messages.success(request, "Investigation report succesfully saved")

        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        toact = request.POST.get('cap')
        toactp = request.POST.get('pap')
        contentact = request.POST.get('reinc_id')
        caact = request.POST.get('ca')
        caactd = request.POST.get('cad')
        paact = request.POST.get('pa')
        paactd = request.POST.get('pat')
        print(toact, toactp, contentact)
        send_mail(
            'Incident Reported',
            #'Incident with ID ' + contentact + ' has been reported and investigated and corrective actionand preventive actions given and assigned. Please check.',
            'Incident with ID '+ contentact +' has been reported and investigated and corrective action' + caact + 'has been assigned to' + cap + 'with deadline' + caactd +'. Preventive action'+ paact + 'with deadline' + paactd+ 'has been assigned to' + pap,
            settings.EMAIL_HOST_USER,
            [toact, toactp]
        )
        
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    #return render(request,"finalinvestigationreport.html")
    return render(request,"finalinvestigationreport.html",{"Forders":finalreportorder})


def actionclosure(request):
    actioncloseorder = Actionclosure.objects.all()

    #return HttpResponse("This is my home page")
    #return render(request, 'whywhyanalysis.html')
    if request.method=="POST":
        actionclose_inc_id=request.POST['actionclose_inc_id']
        actiondonebyname=request.POST['actiondonebyname']
        actiontaken=request.POST['actiontaken']
        completiondate=request.POST['completiondate']
        verify_email=request.POST['verify_email']

        actionclosuredata = Actionclosure(actionclose_inc_id=actionclose_inc_id, actiondonebyname=actiondonebyname, actiontaken=actiontaken, completiondate=completiondate, verify_email=verify_email)  

        actionclosuredata.save()
        messages.success(request, "Action Closure succesfully saved")

        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        tover = request.POST.get('verify_email')
        conver = request.POST.get('actionclose_inc_id')
        conver1 = request.POST.get('actiontaken')
        conver2 = request.POST.get('actiondonebyname')
        conver3 = request.POST.get('completiondate')
        send_mail(
            'Incident Reported',
            'Incident with ID '+ conver +' has been reported and investigated and corrective & Preventive action has been assigned and completed. Action -'+ conver1 + 'has been completed by' + conver2 + 'by' + conver3,
            settings.EMAIL_HOST_USER,
            [tover]
        )
        

    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    return render(request,"actionclosure.html", {"Aorders":actioncloseorder})


def verifyactionclose(request):
    verifyactionorder = Verifyactionclose.objects.all()
    #return HttpResponse("This is my home page")
    #return render(request, 'whywhyanalysis.html')
    if request.method=="POST":
        ver_action_close_inc_id=request.POST['ver_action_close_inc_id'] #this
        inc_closeoropen=request.POST['inc_closeoropen']
        remarks=request.POST['remarks']
        assigner_mail_final=request.POST['assigner_mail_final']

        verifyactionclosedata = Verifyactionclose(ver_action_close_inc_id=ver_action_close_inc_id, inc_closeoropen=inc_closeoropen, remarks=remarks, assigner_mail_final=assigner_mail_final)  

        verifyactionclosedata.save()
        messages.success(request, "Incident Closure succesfully saved")

        #return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        toassign = request.POST.get('assigner_mail_final')
        conver11 = request.POST.get('ver_action_close_inc_id')
        conver22 = request.POST.get('inc_closeoropen')
        conver33 = request.POST.get('remarks')
        send_mail(
            'Incident Reported',
            'Incident with ID '+ conver11 +' has been reported and investigated and corrective & Preventive action has been completed an Verifier has verified them. Status -'+ conver22 + ', Remarks -' + conver33,
            settings.EMAIL_HOST_USER,
            [toassign]
        )
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    #return render(request,"verifyactionclose.html")
    return render(request,"verifyactionclose.html",{"Vorders":verifyactionorder})




def finalreportpdf(request, pk):
    finalreportorder = Finalreport.objects.get(reinc_id=pk)
    print(finalreportorder)
    return render(request, 'finalreportpdf.html', {"finalreportorder":finalreportorder})



def low(request):
    finalreportorder = Finalreport.objects.get(intensity=1)
    return render(request, 'low.html', {"finalreportorder":finalreportorder})
    

def moderate(request):
    finalreportorder = Finalreport.objects.get(intensity=2)
    return render(request, 'low.html', {"finalreportorder":finalreportorder})

def high(request):
    finalreportorder = Finalreport.objects.get(intensity=3)
    return render(request, 'low.html', {"finalreportorder":finalreportorder})

def extreme(request):
    finalreportorder = Finalreport.objects.get(intensity=4)
    return render(request, 'low.html', {"finalreportorder":finalreportorder})


def actionandreport(request):
    actioncloseorder = Actionclosure.objects.all()
    finalreportorder = Finalreport.objects.all()

    return render(request, 'actionandreport.html', {"actioncloseorder":actioncloseorder, "finalreportorder":finalreportorder})




#######################################################################################
#######################################################################################
#######################################################################################

##############TUTION MANAGEMENT SYSTEM#############


def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')



def handleSignupT(request): #adduser
    if request.method=='GET':
        return render(request, 'tutsignup.html')
    if request.method=='POST':
        #Get parameters posted
        username=request.POST['emailsignup']
        firstnamesignup=request.POST['firstnamesignup']
        lastnamesignup=request.POST['lastnamesignup']  
        phonesignup=request.POST['phonesignup']
        passsignup=request.POST['passsignup']
        

        myuser = User.objects.create_user(username, passsignup)
        myuser.person_name=firstnamesignup
        myuser.save()
        messages.success(request, "Your account has been successfully created")

        tosign = request.POST.get('emailsignup')
        print(tosign)
        send_mail(
            'You have signed in successfully.',
            'Go Back to the website to Login.',
            settings.EMAIL_HOST_USER,
            [tosign]
        )
        
        return redirect('/')




def handleSignupS(request): #adduser
    if request.method=='GET':
        return render(request, 'studsignup.html')
    if request.method=='POST':
        #Get parameters posted
        usernamestud=request.POST['emailsignupstud']
        firstnamesignupstud=request.POST['firstnamesignupstud']
        lastnamesignupstud=request.POST['lastnamesignupstud']  
        phonesignupstud=request.POST['phonesignupstud']
        passsignupstud=request.POST['passsignupstud']
        

        myuser = User.objects.create_user(usernamestud, passsignupstud)
        myuser.person_name=firstnamesignupstud
        myuser.save()
        messages.success(request, "Your account has been successfully created")

        tosignstud = request.POST.get('emailsignupstud')
        print(tosignstud)
        send_mail(
            'You have signed in successfully.',
            'Go Back to the website to Login.',
            settings.EMAIL_HOST_USER,
            [tosignstud]
        )
        
        return redirect('/')



def handleLoginT(request):
    if request.method=='GET':
        return render(request, 'tutlogin.html')
        
    if request.method=='POST':
        usernamelogin=request.POST['usernamelogin'] 
        passlogin=request.POST['passlogin']

        user=authenticate(username=usernamelogin, password=passlogin)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('tutordashboard/qk')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('handleLoginT')



def handleLoginS(request):
    if request.method=='GET':
        return render(request, 'studlogin.html')
        
    if request.method=='POST':
        usernameloginstud=request.POST['usernameloginstud'] 
        passloginstud=request.POST['passloginstud']

        user=authenticate(username=usernameloginstud, password=passloginstud)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('studentdashboardpage/<kk>')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('handleLoginS')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')


def tutcreateprofile(request):
    finalprofiletutorder = Finaltutorprofile.objects.all()
    if request.method=="POST":
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
        
        finaltutprofiledata = Finaltutorprofile(inputfirstnamet=inputfirstnamet, inputlastnamet=inputlastnamet, inputemailt=inputemailt, inputphonet=inputphonet, inputtypet=inputtypet, inputaddresst=inputaddresst, inputpict=inputpict, inputcoursest=inputcoursest, inputexperiencet=inputexperiencet, inputaget=inputaget, inputorgt=inputorgt, inputtimet=inputtimet, inputseatt=inputseatt, inputmodet=inputmodet)  

        finaltutprofiledata.save()
        messages.success(request, "Tutor Profile succesfully created and saved")
              
    return render(request,"tutcreateprofile.html",{"Ftutprofileorders":finalprofiletutorder})


def tutorprofile(request, pk):
    finalprofiletutorder = Finaltutorprofile.objects.get(inputemailt=pk)
    print(finalprofiletutorder)
    return render(request, 'tutorprofile.html', {"finalprofiletutorder":finalprofiletutorder})
    #return HttpResponse("This is my home page")
    #return render(request, 'tutorprofile.html')

def tutordashboard(request, qk):
    #return HttpResponse("This is my home page")
    #return render(request, 'tutordashboard.html')
    finalprofiletutorder = Finaltutorprofile.objects.get(inputemailt=qk)
    print(finalprofiletutorder)
    return render(request, 'tutorprofile.html', {"finalprofiletutorder":finalprofiletutorder})

def studcreateprofile(request):
    finalprofilestudorder = Finalstudentprofile.objects.all()
    if request.method=="POST":
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
        
        finalstudprofiledata = Finalstudentprofile(inputfirstnamestu=inputfirstnamestu, inputlastnamestu=inputlastnamestu, inputemailstu=inputemailstu, inputphonestu=inputphonestu, inputtypestu=inputtypestu, inputaddressstu=inputaddressstu, inputclassstu=inputclassstu, inputbranchstu=inputbranchstu, inputexperiencestu=inputexperiencestu, inputagestu=inputagestu, inputgenstu=inputgenstu, inputtimestu=inputtimestu, inputmodestu=inputmodestu)  

        finalstudprofiledata.save()
        messages.success(request, "Tutor Profile succesfully created and saved")
              
    return render(request,"studcreateprofile.html",{"Fstudprofileorders":finalprofilestudorder})


def studentprofile(request, ik):
    finalprofilestudorder = Finalstudentprofile.objects.get(inputemailt=ik)
    print(finalprofilestudorder)
    return render(request, 'studentprofile.html', {"finalprofilestudorder":finalprofilestudorder})
    #return HttpResponse("This is my home page")
    #return render(request, 'tutorprofile.html')

def studentdashboardpage(request, kk):
    #return HttpResponse("This is my home page")
    #return render(request, 'studentdashboardpage.html')
    finalprofiletutorder = Finaltutorprofile.objects.get(inputemailt=kk)
    print(finalprofiletutorder)
    return render(request, 'tutorprofile.html', {"finalprofiletutorder":finalprofiletutorder})

def registernewcourse(request):
    #return HttpResponse("This is my home page")
    #return render(request, 'registernewcourse.html')
    finalregisterstudorder = Finalstudentregister.objects.all()
    if request.method=="POST":
        registernewcontact=request.POST['registernewcontact']
        registernewemail=request.POST['registernewemail']
        studentnotetotutor=request.POST['studentnotetotutor']
        
        finalstudregisterdata = Finalstudentregister(registernewcontact=registernewcontact, registernewemail=registernewemail, studentnotetotutor=studentnotetotutor)  

        finalstudregisterdata.save()
        messages.success(request, "Course Registered Successfully")
              
    return render(request,"registernewcourse.html",{"Fstudregisterorders":finalregisterstudorder})



def editprofilestudent(request):
    #return HttpResponse("This is my home page")
    return render(request, 'editprofilestudent.html')

def editprofiletutor(request):
    #return HttpResponse("This is my home page")
    return render(request, 'editprofiletutor.html')































































































































