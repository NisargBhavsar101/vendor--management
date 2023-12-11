from django.db.models import Avg, Count, F
from django.db import transaction
from .models import Vendor, PurchaseOrder, HistoricalPerformance

@transaction.atomic
def update_vendor_metrics(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')

    # On-Time Delivery Rate
    vendor.on_time_delivery_rate = (
        completed_orders.filter(delivery_date__lte=F('acknowledgment_date')).count() /
        completed_orders.count() * 100 if completed_orders.count() > 0 else 0
    )

    # Quality Rating Average
    vendor.quality_rating_avg = completed_orders.filter(quality_rating__isnull=False).aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

    # Average Response Time
    vendor.average_response_time = (
        completed_orders.filter(acknowledgment_date__isnull=False)
        .aggregate(Avg(F('acknowledgment_date') - F('issue_date')))['acknowledgment_date__avg'].total_seconds() or 0
    )

    # Fulfillment Rate
    vendor.fulfillment_rate = (
        completed_orders.filter(status='completed').count() /
        PurchaseOrder.objects.filter(vendor=vendor).count() * 100 if PurchaseOrder.objects.filter(vendor=vendor).count() > 0 else 0
    )

    vendor.save()

    # Save historical performance record
    HistoricalPerformance.objects.create(
        vendor=vendor,
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=vendor.fulfillment_rate,
    )
