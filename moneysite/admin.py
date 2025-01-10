from django.contrib import admin
from .models import Account

# Register your models here.

from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'transaction_type', 'date')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
