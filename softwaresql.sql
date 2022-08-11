--CREATE DATABASE TutionManagementSoftware
use TutionManagementSoftware

create table signup(
name varchar(50) not null, --Name
email varchar(100) not null , --Email address
phone numeric(15) not null, --Phone
password varchar(25) not null, --Password
category varchar(25) not null, --Category
primary key(email,phone)
);

create table tutorprofile(
tutorname varchar(50) not null, --TutorName
tutoremail varchar(100) primary key, --TutorEmail address
tutorphone numeric(15) not null, --Phone
tutoraddress varchar(200) not null, --address
tutorpicturelink varchar(100) not null, --picturelink
cources varchar(50) not null, --Courses
experience int not null, --experience
age int not null, --age
organisationlink varchar(100) , --organisationlink
linkedin varchar(100) , --linkedinlink
tutortimings time not null, --timings
seats int not null, --seats
mode varchar(50) not null, --modeofteaching
constraint fk_emailphone foreign key(tutoremail, tutorphone) references signup(email, phone)
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