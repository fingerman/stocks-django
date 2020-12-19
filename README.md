# STOCKS CRM

This is built from scratch CRM system based on Django 3.1

This basic CRM is divided into Companies, Suppliers and Products.  

##### Relations:  
A Company is related to multiple Products
Multiple products are related to Multiple suppliers e.g. several suppliers offer same product and vice versa.

There is public part. Visitors can view lists of the companies, suppliers and products.   
Logged users access detailed views of all items and can add new items.   
Logged users can edit only items, which were created by them. 'permission denied' emerges
if they try to access an edit form of item, created by another user, directly from the url.   


##### Features:

Company Details:  
* Name
* Segment
* Address
* Segment
* Email (emailType)
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