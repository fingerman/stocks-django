from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from stocks.records.models import Company, Product, Supplier


class CompaniesListView(views.ListView):
    context_object_name = 'company_list'
    template_name = 'records/company_list.html'
    model = Company


class CompanyDetailsView(views.DetailView):
    template_name = 'records/company_details.html'
    model = Company


class CreateCompanyView(views.CreateView):
    model = Company
    template_name = 'records/company_create.html'
    fields = '__all__'

    def get_success_url(self):
        # return reverse('index')
        return reverse('company details', kwargs={'pk': self.object.pk})


class CompanyUpdateView(views.UpdateView):
    fields = '__all__'
    model = Company
    template_name = 'records/company_edit.html'

    def get_success_url(self):
        return reverse('company details', kwargs={'pk': self.object.pk})


class CompanyDeleteView(views.DeleteView):
    fields = '__all__'
    model = Company
    template_name = 'records/company_delete.html'
    success_url = reverse_lazy('index')


################# Products


class ProductsListView(views.ListView):
    context_object_name = 'product_list'
    template_name = 'records/product_list.html'
    model = Product


class ProductDetailsView(views.DetailView):
    template_name = 'records/product_details.html'
    model = Product


class ProductCreateView(views.CreateView):
    model = Product
    template_name = 'records/product_create.html'
    fields = '__all__'

    def get_success_url(self):
        # return reverse('index')
        return reverse('product details', kwargs={'pk': self.object.pk})


class ProductUpdateView(views.UpdateView):
    fields = '__all__'
    model = Product
    template_name = 'records/product_edit.html'

    def get_success_url(self):
        return reverse('product details', kwargs={'pk': self.object.pk})


class ProductDeleteView(views.DeleteView):
    fields = '__all__'
    model = Product
    template_name = 'records/product_delete.html'
    success_url = reverse_lazy('product list')

################# Suppliers


class SupplierListView(views.ListView):
    context_object_name = 'supplier_list'
    template_name = 'records/supplier_list.html'
    model = Supplier


class SupplierDetailsView(views.DetailView):
    template_name = 'records/supplier_details.html'
    model = Supplier


class SupplierCreateView(views.CreateView):
    model = Supplier
    template_name = 'records/supplier_create.html'
    fields = '__all__'

    def get_success_url(self):
        # return reverse('index')
        return reverse('supplier details', kwargs={'pk': self.object.pk})


class SupplierUpdateView(views.UpdateView):
    fields = '__all__'
    model = Supplier
    template_name = 'records/supplier_edit.html'

    def get_success_url(self):
        return reverse('supplier details', kwargs={'pk': self.object.pk})


class SupplierDeleteView(views.DeleteView):
    fields = '__all__'
    model = Supplier
    template_name = 'records/supplier_delete.html'
    success_url = reverse_lazy('supplier list')
