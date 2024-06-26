from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer, MenuItemSerializer2,MenuItemSerializer3, MenuItemSerializer4
from rest_framework import status
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer3
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
        queryset = MenuItem.objects.all()
        serializer_class=MenuItemSerializer
        
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET','POST'])
def menu_items(request):
    if request.method == "GET":
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category');
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(title__startswith=search)
            
        serialized_item = MenuItemSerializer4(items,many=True, context={'request':request})
        return Response(serialized_item.data)
    if request.method == "POST":
        serialized_item = MenuItemSerializer4(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

from django.shortcuts import get_object_or_404
@api_view()
def single_item(request,pk):
    item = get_object_or_404(MenuItem,pk=pk)
    serialized_item = MenuItemSerializer2(item)
    return Response(serialized_item.data)

from .models import Category 
from .serializers import CategorySerializer
@api_view()
def category_detail(request,pk):
    category = get_object_or_404(Category,pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)