from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from .utils import update_vendor_metrics
from django.http import Http404

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()    
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()  # Use HistoricalPerformance model
    serializer_class = HistoricalPerformanceSerializer

    def retrieve(self, request, *args, **kwargs):
        vendor = get_object_or_404(Vendor, pk=kwargs['pk'])  # Retrieve Vendor instance
        historical_performance = HistoricalPerformance.objects.filter(vendor=vendor).latest('date')  # Get latest performance
        serializer = self.get_serializer(historical_performance)
        return Response(serializer.data)

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
class HistoricalPerformanceListCreateView(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
class HistoricalPerformanceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer    

class AcknowledgePurchaseOrderView(generics.RetrieveUpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        update_vendor_metrics(instance.vendor)
