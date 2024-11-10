from django.shortcuts import render
from rest_framework import viewsets, permissions,generics
from .models import Course, Category
from .serializers import CategorySerializer, CourseSerializer

# Create your views here.

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True).all()
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True).all()
    serializer_class = CourseSerializer