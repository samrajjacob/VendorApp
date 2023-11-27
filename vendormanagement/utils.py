from django.db.models import Count, Avg
from django.utils import timezone

def update_vendor_performance_metrics(vendor):
    completed_pos = vendor.purchaseorder_set.filter(status='completed')
    on_time_deliveries = completed_pos.filter(delivery_date__lte=timezone.now())
    vendor.on_time_delivery_rate = on_time_deliveries.count() / completed_pos.count() * 100 if completed_pos.count() > 0 else 0

    completed_pos_with_ratings = completed_pos.exclude(quality_rating__isnull=True)
    vendor.quality_rating_avg = completed_pos_with_ratings.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

    acknowledged_pos = completed_pos.filter(acknowledgment_date__isnull=False)
    response_times = [(pos.acknowledgment_date - pos.issue_date).total_seconds() for pos in acknowledged_pos]
    vendor.average_response_time = sum(response_times) / acknowledged_pos.count() if acknowledged_pos.count() > 0 else 0

    completed_pos_without_issues = completed_pos.filter(status='completed')
    vendor.fulfillment_rate = (completed_pos_without_issues.count() / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0

    vendor.save()
