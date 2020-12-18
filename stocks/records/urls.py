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
    path('<int:pk>/', views.ProductDetailsView.as_view(), name='product details'),
    path('create/', views.ProductCreateView.as_view(), name='product create'),
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='product edit'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product delete'),

    # suppliers
)