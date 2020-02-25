select * from salesman;
select * from customer;
select * from orders;

--Write a SQL statement to prepare a list with salesman name, customer name and their cities, 
--for the salesmen and customer who belongs to the same city.

select s.fullname salesman_name,c.cust_name,c.city 
from salesman as s,customer as c
where s.city = c.city;

--Write a SQL statement to make a list with order no, purchase amount, customer name and their cities 
--for those orders which order amount between 500 and 2000


select o.ord_no, o.purch_amt, c.cust_name, c.city 
from orders o , customer c
where o.customer_id = c.customer_id and o.purch_amt between 500 and 2000;

--Write a SQL statement to know which salesman are working for which customer.

select s.fullname as salesman, c.cust_name as customer
from salesman s, customer c
where s.salesman_id = c.salesman_id;
-------------------------or------------------------------
select s.fullname as salesman, c.cust_name as customer
from customer c
inner join salesman s
on s.salesman_id = c.salesman_id;


--Write a SQL statement to find the list of customers who appointed a salesman for their 
--jobs who gets a commission from the company is more than 12%. 

select  c.cust_name, c.city, s.commision, s.fullname 
from customer c
inner join salesman s
on s.salesman_id = c.salesman_id 
where s.commision > 0.12;

--Write a SQL statement to find the list of customers who appointed a salesman 
--for their jobs who does not live in the same city where their customer lives,
--and gets a commission is above 12% .

select  c.cust_name, c.city, s.city, s.commision, s.fullname 
from customer c
inner join salesman s
on s.salesman_id = c.salesman_id 
where s.commision > 0.12 and s.city <> c.city;


--Write a SQL statement to find the details of a order 
--i.e. order number, order date, amount of order, which customer gives the order 
--and which salesman works 
--for that customer and how much commission he gets for an order.

select o.ord_no, o.ord_date, o.purch_amt , c.cust_name, s.fullname, s.commision
from orders o
inner join customer c
on c.customer_id = o.customer_id
inner join salesman s
on o.salesman_id = s.salesman_id;

--Write a SQL statement to make a join on the tables salesman, customer and orders 
--in such a form that 
--the same column of each table will appear once and only the relational rows will come. 
--Try again!!!!!!!!!!!!!!
select *
from orders o
inner join customer c 
on c.customer_id = o.customer_id
inner join salesman s 
on s.salesman_id = o.salesman_id

--Write a SQL statement to make a list in ascending order for the customer who works 
--either through a salesman or by own.

select c.customer_id, c.cust_name, c.city, c.grade, s.fullname, s.city from customer c
left join salesman s
on c.salesman_id = s.salesman_id
order by c.customer_id

 --Write a SQL statement to make a list in ascending order for the customer who holds a 
 --grade less than 300 and works either through a salesman or by own. 

 select c.customer_id, c.cust_name, c.city, c.grade, s.fullname, s.city from customer c
left join salesman s
on c.salesman_id = s.salesman_id
where c.grade < 300
order by c.customer_id

--Write a SQL statement to make a report with customer name, city, order number,
--order date, and order amount in ascending order according to the order date to 
--find that either any of the existing 
--customers have placed no order or placed one or more orders.

select c.customer_id, c.cust_name, c.city, o.ord_no ,o.ord_date, o.purch_amt    
from customer c
left outer join orders o
on o.customer_id = c.customer_id
order by o.ord_date

--Write a SQL statement to make a report with 
--customer name, city, order number, order date, order amount salesman name 
--and commission to find that either any of the existing customers have placed no order 
--or placed one or more orders by their salesman or by own.

select c.customer_id, c.cust_name, c.city, o.ord_no ,o.ord_date, o.purch_amt ,
s.fullname, s.commision
from customer c
left outer join orders o
on o.customer_id = c.customer_id
left outer join salesman s
on s.salesman_id = o.salesman_id

--Write a SQL statement to make a list in ascending order for the 
--salesmen who works either for one or more customer or not
--yet join under any of the customers.
--, s.city, s.commision, c.cust_name

select distinct s.fullname
from salesman s
left outer join customer c
on c.salesman_id =  s.salesman_id
order by s.fullname


