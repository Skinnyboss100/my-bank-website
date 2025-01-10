from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
# Create your views here.

def account(request):
    user_balance = 2500.75  # Fetch this dynamically from your database
    return render(request, 'moneysite/account.html', {'balance': user_balance})

def transactions(request):
    return render(request,'moneysite/transactions.html')

def account_balance_view(request):
    account = Account.objects.get(user=request.user)
    return render(request, 'account.html', {'account': account})
