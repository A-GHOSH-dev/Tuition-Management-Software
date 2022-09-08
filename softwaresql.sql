CREATE DATABASE TutionManagementSoftware
use TutionManagementSoftware

create table Finaltutorprofile(
inputfirstnamet varchar(50) not null, --Name
inputlastnamet varchar(50) not null, --Name
idtutor int not null primary key,
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
);

create table Finalstudentprofile(
inputfirstnamestu varchar(50) not null, --TutorName
inputlastnamestu varchar(50) not null, --TutorName
idstudent int not null primary key,
inputemailstu varchar(100) not null, --TutorEmail address
inputphonestu numeric(15) not null, --Phone
inputtypestu varchar(50) not null, --Courses
inputaddressstu varchar(200) not null, --address
inputclassstu varchar(50) not null, --Courses
inputbranchstu varchar(100) not null, --organisationlink
inputexperiencestu varchar(100) not null, --organisationlink
inputagestu int not null, --age
inputgenstu varchar(10) not null, --organisationlink
inputtimestu varchar(100) not null, --organisationlink
inputmodestu varchar(100) not null, --linkedinlink

);

create table Finalstudentregister(
registernewid numeric(20) not null,
registernewcontact numeric(15) not null, --StudentName
registernewemail varchar(100) not null primary key, --StudentEmail address
studentnotetotutor varchar(200) not null, --address
tutoridnew varchar(500) not null,
tutornewemail varchar(300) not null,
coursesregistered varchar(200) not null,

);


DROP TABLE Finaltutorprofile;
DROP TABLE Finalstudentregister;
DROP TABLE Finalstudentprofile;


select * from Finalstudentregister;
SELECT 
    COUNT(inputfirstnamestu)
FROM
    Finalstudentprofile;
