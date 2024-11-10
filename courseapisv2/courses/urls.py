from django.urls import path, include, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('courses', views.CategoryViewSet, basename='courses')

urlpatterns = [
    path('',include(router.urls))
]
