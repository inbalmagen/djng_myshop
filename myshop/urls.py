
from django.contrib import admin
from django.urls import include, path

from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('categories/', views.category_list, name='category-list'),
]
