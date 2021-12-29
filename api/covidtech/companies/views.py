from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from django.core.mail import send_mail
# Create your views here.


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("last_update")
    pagination_class = PageNumberPagination


@api_view(http_method_names=["POST"])
def send_company_email(req):
    send_mail(
        subject="New company added",
        message=f"{req.data['name']} has been added to the database",
        from_email="gabrielpitaromero@gmx.com",
        recipient_list=["gabrielpitaromero@gmx.com"]
    )
    return Response({"status": "success", "message": "Email sent"}, status=200)
