from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
# Create your views here.

class StoreList(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class Product(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class Purchase(viewsets.ModelViewSet):
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSerializer