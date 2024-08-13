from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker.models import Transaction
from tracker.filters import TransactionFilter

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')


@login_required
def transaction_list(request):
    transaction_filter = TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related('Category')
    )
    total_income = transaction_filter.qs.get_total_income()
    total_expense = transaction_filter.qs.get_total_expense()
    context = {
        'filter': transaction_filter,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_income': float(total_income) - float(total_expense)
    }

    if request.htmx:
        return render(request, 'tracker/partials/transaction-container.html', context)

    return render(request, 'tracker/transaction-list.html', context)
    
    