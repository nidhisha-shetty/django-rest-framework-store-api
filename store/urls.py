# api/urls.py
from django.urls import path, include
from rest_framework import routers
from store import views

router =routers.DefaultRouter()
router.register('store', views.StoreList)
router.register('product', views.Product)
router.register('purchase', views.Purchase)

urlpatterns = [
    path('', include(router.urls))
]