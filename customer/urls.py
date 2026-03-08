from django.urls import path
from . import views
from .views import CustomerDestroyView, CustomerUpdateView, CustomerRUDView

urlpatterns = [
    path('produce_consumer/', views.produce_consumer, name='produce_consumer'),
    path('destroy/<int:pk>/', CustomerDestroyView.as_view(), name='customer-destroy'),
    path('update/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('rud/<int:pk>/', CustomerRUDView.as_view(), name='customer-rud'),
]