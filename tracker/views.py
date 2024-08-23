from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker.models import Transaction
from tracker.filters import TransactionFilter
from tracker.forms import TransactionForm

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')


@login_required
def transaction_list(request):
    transaction_filter = TransactionFilter(
        request.GET,# query parameters from the URL, such as filters which we requested using htmx
        queryset=Transaction.objects.filter(user=request.user).select_related('category')
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

    return render(request, 'tracker/transactions-list.html', context)
    
    

@login_required
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            context = {'message': "Transaction was added successfully!"}
            return render(request, 'tracker/partials/transaction-success.html', context)

    context = {'form': TransactionForm()}
    return render(request, 'tracker/partials/create-transaction.html', context)