from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField

UserModel = get_user_model()


class Company(models.Model):
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    country = CountryField()
    segment = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = MoneyField(max_digits=15, decimal_places=2, default_currency='EUR')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField(default="Description")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    email = models.EmailField(null=True)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
