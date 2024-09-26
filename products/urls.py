
from django.contrib import admin
from django.urls import include, path

from products import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
     path('', views.product_list, name="product_list"),
     path('<int:id>/', views.product_detail, name="product_detail"),

]
