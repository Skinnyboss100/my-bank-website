from django.urls import path
from . import views

urlpatterns = [
    path('',views.account,name='moneysite-account' ),
    path('transactions/',views.transactions,name='transcations-page'),
    
]