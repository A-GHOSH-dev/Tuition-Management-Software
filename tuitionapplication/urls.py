from django.contrib import admin
from django.urls import path, include
from tuitionapplication import views

admin.site.site_header ="Developer Ananya Ghosh"
admin.site.site_title= "Welcome to my dashboard"
admin.site.index_title="Welcome to my portal"

urlpatterns = [
    
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('low', views.low, name='low'),
    path('high', views.high, name='high'),
    path('moderate', views.moderate, name='moderate'),
    path('extreme', views.extreme, name='extreme'),
    #path('home', views.home, name='home'),
   # path('signup', views.signup, name='signup'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('adduser', views.adduser, name='adduser'),
    path('incidentreport', views.incidentreport, name='incidentreport'),
    path('assignleadinvestigator', views.assignleadinvestigator, name='assignleadinvestigator'),
    path('allincidentslist', views.allincidentslist, name='allincidentslist'),
    path('whywhyanalysis', views.whywhyanalysis, name='whywhyanalysis'),
    path('specialanalysis', views.specialanalysis, name='specialanalysis'),
    path('finalinvestigationreport', views.finalinvestigationreport, name='finalinvestigationreport'),
    path('actionclosure', views.actionclosure, name='actionclosure'),
    path('verifyactionclose', views.verifyactionclose, name='verifyactionclose'),
    path('incidentenquiry', views.incidentenquiry, name='incidentenquiry'),
    path('profilepage', views.profilepage, name='profilepage'),
    path('actionandreport', views.actionandreport, name='actionandreport'),
    path('finalreportpdf/<str:pk>', views.finalreportpdf, name='finalreportpdf'),
    #path('payment', views.payment, name='payment')
    
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    
    
    path('', views.index, name='index'),
    path('studentdashboardpage', views.studentdashboardpage, name='studentdashboardpage'),
    path('studentprofile', views.studentprofile, name='studentprofile'),
    path('tutlogin', views.handleLoginT, name='handleLoginT'),
    path('studlogin', views.handleLoginS, name='handleLoginS'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('tutordashboard', views.tutordashboard, name='tutordashboard'),
    path('tutorprofile', views.tutorprofile, name='tutorprofile'),
    path('tutsignup', views.handleSignupT, name='handleSignupT'),
    path('studsignup', views.handleSignupS, name='handleSignupS'),
    path('registernewcourse', views.registernewcourse, name='registernewcourse'),
    path('editprofilestudent', views.editprofilestudent, name='editprofilestudent'),
    path('editprofiletutor', views.editprofiletutor, name='editprofiletutor'),
    path('tutcreateprofile', views.tutcreateprofile, name='tutcreateprofile'),
    path('studcreateprofile', views.studcreateprofile, name='studcreateprofile')
    

]