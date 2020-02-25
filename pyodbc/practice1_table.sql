create database practice1

use practice1

create table salesman
(
salesman_id int primary key identity(5001,1),
fullname char(15) not null,
city char(10) ,
commision float ,

);


insert into salesman values ('James Hoog','New York',0.15);
insert into salesman values ('Nail Knite','Paris',0.13);
insert into salesman values ('Pit Alex','London',0.11);
insert into salesman values ('Mc Lyon','Paris',0.14);
insert into salesman values ('Paul Adam','Rome',0.13);
insert into salesman values ('Lauson Hen','San Jose',0.12);

select * from salesman

------------------------------------------------------------------------------------------

create table customer
(
customer_id int primary key identity(3001,1),
cust_name char(15) not null,
city char(10) ,
grade int ,
salesman_id int foreign key references salesman(salesman_id),

);


insert into customer values ('Nick Rimando','New York',100,5001);
insert into customer values ('Brad Davis','New York',200,5001);
insert into customer values ('Graham Zusi','California',200,5002);
insert into customer values ('Julian Green','London',300,5002);
insert into customer values ('Fabian Johnson','Paris',300,5006);
insert into customer values ('Geoff Cameron','Berlin',100,5003);
insert into customer values ('Jozy Altidor','Moscow',200,5003);
insert into customer values ('Brad Guzan','London',null,5005);


select * from customer

--------------------------------------------------------------------------------------------
create table orders
(
ord_no int primary key identity(7001,1),
purch_amt float ,
ord_date date ,
customer_id int foreign key references customer(customer_id),
salesman_id int foreign key references salesman(salesman_id),

);

insert into orders values (150.5,'2012-10-05',3005,5002);
insert into orders values (270.65,'2012-09-10',3001,5005);
insert into orders values (65.26,'2012-10-05',3002,5001);
insert into orders values (110.5,'2012-08-17',3006,5003);
insert into orders values (948.5,'2012-09-10',3005,5002);
insert into orders values (2400.6,'2012-07-27',3007,5001);
insert into orders values (5760,'2012-09-10',3002,5001);
insert into orders values (1983.43,'2012-10-10',3004,5006);
insert into orders values (2480.4,'2012-10-10',3006,5003);
insert into orders values (250.45,'2012-06-27',3008,5002);
insert into orders values (75.29,'2012-08-17',3003,5006);
insert into orders values (3045.6,'2012-04-25',3002,5001);


select * from orders