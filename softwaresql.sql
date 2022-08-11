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
primary key(inputemailt)
);

create table Finalstudentprofile(
inputfirstnamestu varchar(50) not null, --TutorName
inputlastnamestu varchar(50) not null, --TutorName
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
primary key(inputemailstu)
);

create table Finalstudentregister(
registernewcontact numeric(15) not null, --StudentName
registernewemail varchar(100) not null, --StudentEmail address
studentnotetotutor varchar(200) not null, --address
constraint fk_emailphone foreign key(registernewemail) references Finalstudentprofile(inputemailstu)
);


DROP TABLE Finaltutorprofile;
DROP TABLE Finalstudentprofile;
DROP TABLE Finalstudentregister;
