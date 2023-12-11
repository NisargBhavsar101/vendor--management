from django.urls import path
# from .views import MyView
from .views import (
    VendorListCreateView,
    VendorRetrieveUpdateDeleteView,
    PurchaseOrderListCreateView,
    PurchaseOrderRetrieveUpdateDeleteView,
    VendorPerformanceView,
    AcknowledgePurchaseOrderView,
    HistoricalPerformanceListCreateView,
    HistoricalPerformanceRetrieveUpdateDeleteView
)

urlpatterns = [
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchase-order-retrieve-update-delete'),
    path('vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),
    path('historical_performance/', HistoricalPerformanceListCreateView.as_view(), name='historical-performance-list-create'),  # Add this line
    path('historical_performance/<int:pk>/', HistoricalPerformanceRetrieveUpdateDeleteView.as_view(), name='historical-performance-retrieve-update-delete'),  # Add this line

]
