create database dock_engine;
use dock_engine;


start transaction;

create table SLogin(
Gid varchar(20) primary key,
Pass char(40) not null);


create table Groups(
Gid varchar(20) not null,
Rollno int(5) primary key,

Sname varchar(30) not null,
foreign key(Gid) references SLogin(Gid));



create table Project(
Gid varchar(20) not null,
Pid varchar(20) primary key,
ProjectName varchar(30) not null,
Gitlink varchar(100) not null,
foreign key(Gid) references SLogin(Gid));

create table Image(
Gid varchar(20) not null,
Pid varchar(20) not null unique key,
Imglink varchar(100) not null,
foreign key(Gid) references SLogin(Gid),
foreign key(Pid) references Project(Pid),
primary key(Gid,Pid));

create table TLogin(
Tid varchar(20) primary key,
Pass char(40) not null,
Tname varchar(30) not null);

commit;

