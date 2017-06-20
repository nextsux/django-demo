from django.shortcuts import render
from django.views.generic import ListView
from app1.models import Customer

from rest_framework import viewsets, serializers


class CustomerList(ListView):
    model = Customer
    template_name = 'app1/vypis_zakazniku.html'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =  '__all__' 


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
