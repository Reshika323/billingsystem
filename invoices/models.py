from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    customer_name = models.CharField(max_length=255)
    invoice_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Invoice #{self.id} for {self.customer_name}"

    def total_amount(self):
        # Sum total of all related InvoiceItems
        return sum(item.total() for item in self.items.all())

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.description} ({self.quantity} @ {self.unit_price})"
