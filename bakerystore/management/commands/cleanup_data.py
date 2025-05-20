from django.core.management.base import BaseCommand
from bakerystore.models import Order, OrderList, Bill
from django.db import transaction

class Command(BaseCommand):
    help = 'Clean up invalid data references'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            # Clean up OrderList entries with invalid order references
            invalid_orderlists = OrderList.objects.exclude(
                order_id__in=Order.objects.values_list('id', flat=True)
            )
            if invalid_orderlists.exists():
                self.stdout.write(f'Deleting {invalid_orderlists.count()} invalid OrderList entries')
                invalid_orderlists.delete()

            # Clean up Bill entries with invalid order references
            invalid_bills = Bill.objects.exclude(
                order_id__in=Order.objects.values_list('id', flat=True)
            )
            if invalid_bills.exists():
                self.stdout.write(f'Deleting {invalid_bills.count()} invalid Bill entries')
                invalid_bills.delete()

            self.stdout.write('Data cleanup completed')
