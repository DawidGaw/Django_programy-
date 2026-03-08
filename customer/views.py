from django.shortcuts import render, redirect
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import generics

def produce_consumer(request):
    if request.method == 'POST':
        Customer.objects.create(name = 'Generated Customer')
        return redirect("produce_consumer")
    customers = Customer.objects.all()
    return render(request, 'customer/produce_consumer.html', {'customers': customers})

class CustomerDestroyView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdateView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

