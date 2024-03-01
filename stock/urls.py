from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from product.views import ProductViewSet

routers = routers.DefaultRouter()
routers.register("product", ProductViewSet, basename="product")

urlpatterns = [
    path('', include(routers.urls)),

    path('admin/', admin.site.urls),
]
