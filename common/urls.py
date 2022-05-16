from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name="index"),
    path('about-us/',views.about_us,name="about-us"),
    path('contact/', views.contact, name="contact"),
    path('products/', views.product, name="product-list"),
    path('account/',views.accounts, name="accounts"),
    path('<slug:category_slug>/', views.product, name="product_list_by_category"),
]