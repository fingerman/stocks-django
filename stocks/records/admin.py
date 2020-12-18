from django.contrib import admin
from .models import Company, Product, Supplier


class ProductInline(admin.StackedInline):
    model = Product


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'address', 'segment', 'country', 'email', 'description')
    inlines = (ProductInline,)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'company', 'description')


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'email')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
