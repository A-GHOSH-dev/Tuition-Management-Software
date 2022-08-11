CREATE DATABASE TutionManagementSoftware
use TutionManagementSoftware

create table Finaltutorprofile(
inputfirstnamet varchar(50) not null, --Name
inputlastnamet varchar(50) not null, --Name
inputemailt varchar(100) not null , --Email address
inputphonet numeric(15) not null, --Phone
inputtypet varchar(25) not null, --Category
inputaddresst varchar(100) not null , --Email address
inputpict varchar(100) not null , --Email address
inputcoursest varchar(100) not null , --Email address
inputexperiencet varchar(100) not null , --Email address
inputaget numeric(15) not null, --Phone
inputorgt varchar(100) not null , --Email address
inputtimet varchar(100) not null , --Email address
inputseatt numeric(15) not null, --Phone
inputmodet varchar(50) not null, --Name
primary key(inputemailt,inputphonet)
);

create table Finalstudentprofile(
inputfirstnamestu varchar(50) not null, --TutorName
inputlastnamestu varchar(50) not null, --TutorName
inputemailstu varchar(100) not null, --TutorEmail address
inputphonestu numeric(15) not null, --Phone
inputtypestu varchar(50) not null, --Courses
inputaddressstu varchar(200) not null, --address
inputclassstu varchar(50) not null, --Courses
inputbranchstu varchar(100) , --organisationlink
inputexperiencestu varchar(100) , --organisationlink
inputagestu int not null, --age
inputgenstu varchar(10) not null, --organisationlink
inputtimestu varchar(100) not null, --organisationlink
inputmodestu varchar(100) not null, --linkedinlink
primary key(inputemailstu,inputphonestu)
);

create table studentprofile(
studentname varchar(50) not null, --StudentName
studentemail varchar(100) primary key, --StudentEmail address
studentphone numeric(15) not null, --Phone
studentaddress varchar(200) not null, --address
studentpicturelink varchar(100) not null, --picturelink
class int not null, --class
school varchar(100) not null, --school
studenttimings time not null --timings
constraint fk_emailphone1 foreign key(studentemail, studentphone) references signup(email, phone)
);

create table registercourses(
message varchar(500), --message_to_tutor
requirements varchar(100), --requirements_from_student
studentemail varchar(100),
tutoremail varchar(100),
constraint fk_emailstudent foreign key(studentemail) references studentprofile(studentemail),
constraint fk_emailtutor foreign key(tutoremail) references tutorprofile(tutoremail)
);