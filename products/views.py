from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from products.models import Category, Product
from products.serializer import CategorySerializer, ProductSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product


@api_view(['GET', 'POST'])
def product_list(request):
    # Handle GET request: Return list of all products (excluding soft-deleted ones)
    if request.method == 'GET':
        search_query = request.GET.get('search', '').strip()  # Get search query from request and strip whitespace
        products = Product.objects.filter(is_deleted=False)  # Exclude deleted products

        if search_query:
            # Filter products based on the search query (case-insensitive and allows 1 letter)
            products = products.filter(name__icontains=search_query) | products.filter(description__icontains=search_query)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    # Handle POST request: Create a new product
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def category_list(request):
    # Handle GET request: Return list of all categories
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)  # Serialize the data
        return Response(serializer.data)
    
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    """
    Retrieve, update or delete a product.
    """
    product = get_object_or_404(Product, id=id)

    if request.method == 'GET':
        # Retrieve single product details
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update the product
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Soft delete the product (set is_deleted to True)
        product.is_deleted = True
        product.save()  # Save the change to the database
        return Response(status=status.HTTP_204_NO_CONTENT)