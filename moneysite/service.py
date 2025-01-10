from .models import Account

def update_balance(user, amount, transaction_type):
    account = Account.objects.get(user=user)
    if transaction_type == 'credit':
        account.balance += amount
    elif transaction_type == 'debit' and account.balance >= amount:
        account.balance -= amount
    else:
        raise ValueError("Insufficient funds or invalid transaction type.")
    account.save()
