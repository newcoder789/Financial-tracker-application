from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker.models import Transaction

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')


@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    # request.user tells us the user associated with request can be authocanticated and not auto
    context = {'transactions':transactions} 
    
    
    return render(request, 'tracker/transaction-list.html', context)
    
    