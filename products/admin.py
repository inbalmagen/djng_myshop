from django.contrib import admin
from .models import Product, Category

# Inline admin to show products within categories
class ProductInline(admin.TabularInline):
    model = Product.categories.through  # Use the many-to-many relationship table
    extra = 1  # Number of empty forms for adding new products

# Custom CategoryAdmin to display products inline
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

# Register your models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
