from django.contrib import admin
from django.urls import path, include
from tuitionapplication import views

admin.site.site_header ="Developer Ananya Ghosh"
admin.site.site_title= "Welcome to my dashboard"
admin.site.index_title="Welcome to my portal"

urlpatterns = [
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    
    
    path('', views.index, name='index'),
    path('studentdashboardpage/<str:ik>', views.studentdashboardpage, name='studentdashboardpage'),
    path('studentprofile/<str:ik>', views.studentprofile, name='studentprofile'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('login', views.handleLogin, name='handleLogin'),
    path('tutordashboard/<str:pk>', views.tutordashboard, name='tutordashboard'),
    path('tutorprofile/<str:pk>', views.tutorprofile, name='tutorprofile'),
    path('registernewcourse', views.registernewcourse, name='registernewcourse'),
    path('editprofilestudent', views.editprofilestudent, name='editprofilestudent'),
    path('editprofiletutor', views.editprofiletutor, name='editprofiletutor'),
    path('tutcreateprofile', views.tutcreateprofile, name='tutcreateprofile'),
    path('studcreateprofile', views.studcreateprofile, name='studcreateprofile'),
    path('studentlist', views.studentlist, name='studentlist'),
    path('tutorlist', views.tutorlist, name='tutorlist'),
    path('searchpage', views.searchpage, name='searchpage'),
    path('tutorprofileview/<str:pk>', views.tutorprofileview, name='tutorprofileview'),
    path('studentprofileview/<str:ik>', views.studentprofileview, name='studentprofileview'),
    

]