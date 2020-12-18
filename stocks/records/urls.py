from django.urls import path
from . import views


urlpatterns = (
    # companies
    path('', views.CompaniesListView.as_view(), name='index'),
    path('<int:pk>/', views.CompanyDetailsView.as_view(), name='company details'),
    path('create/', views.CreateCompanyView.as_view(), name='company create'),
    path('edit/<int:pk>/', views.CompanyUpdateView.as_view(), name='company edit'),
    path('delete/<int:pk>/', views.CompanyDeleteView.as_view(), name='company delete'),

    # products
    path('products/', views.ProductsListView.as_view(), name='product list'),
    path('products/<int:pk>/', views.ProductDetailsView.as_view(), name='product details'),
    path('products/create/', views.ProductCreateView.as_view(), name='product create'),
    path('products/edit/<int:pk>/', views.ProductUpdateView.as_view(), name='product edit'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product delete'),

    # suppliers
    path('supplier/', views.SupplierListView.as_view(), name='supplier list'),
    path('supplier/<int:pk>/', views.SupplierDetailsView.as_view(), name='supplier details'),
    path('supplier/create/', views.SupplierCreateView.as_view(), name='supplier create'),
    path('supplier/edit/<int:pk>/', views.SupplierUpdateView.as_view(), name='supplier edit'),
    path('supplier/delete/<int:pk>/', views.SupplierDeleteView.as_view(), name='supplier delete'),
)