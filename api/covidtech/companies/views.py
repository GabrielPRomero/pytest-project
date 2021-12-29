from django.shortcuts import render

from .models import Company
from .serializers import CompanySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("last_update")
    pagination_class = PageNumberPagination