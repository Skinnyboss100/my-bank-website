from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} - ${self.balance}"


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]

    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount} ({self.transaction_type})"
