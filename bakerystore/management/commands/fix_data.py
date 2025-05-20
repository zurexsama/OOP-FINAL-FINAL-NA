from django.core.management.base import BaseCommand
from bakerystore.models import Bill, Order
from django.db import transaction

class Command(BaseCommand):
    help = 'Fix data integrity issues between Bill and Order'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            # Find bills with invalid order references
            invalid_bills = Bill.objects.exclude(order_id__in=Order.objects.values_list('id', flat=True))
            
            if invalid_bills.exists():
                self.stdout.write(f'Found {invalid_bills.count()} invalid bills')
                invalid_bills.delete()
                self.stdout.write('Deleted invalid bills')
            else:
                self.stdout.write('No invalid bills found')
