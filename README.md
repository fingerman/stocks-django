# STOCKS CRM

This is built from scratch CRM system based on Django 3.1

This basic CRM is divided into Companies, Suppliers and Products.

There is public part. Visitors can view lists of the companies, suppliers and products. 
They need to be logged in to see detail views, edit, create or delete the entries. 


Features:

Company Details:  
* Name
* Segment
* Address
* Segment
* Email
* Description

Supplier  

* Name
* Email (emailType)
* Address
* Products (ManyToMany)

Product

* Name
* Price (Money Field)
* Company (Many To One)
* Description