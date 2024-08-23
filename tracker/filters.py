import django_filters
from django import forms
from tracker.models import Transaction ,Category

class TransactionFilter(django_filters.FilterSet):
    transaction_type = django_filters.ChoiceFilter(#This filter allows filtering based on a set of predefined choices
        choices = Transaction.TRANSACTION_TYPE_CHOICES, #tuple
        field_name = 'type', #Specifies the model field that this filter should be applied to 
        lookup_expr = 'iexact', #  lookup_expr argument specifies the type of query that should be performed. 
        #iexact-filter will match values in a case-insensitive manner.
        empty_label = 'Any',            
    )
    start_date = django_filters.DateFilter(
        field_name='date', 
        lookup_expr='gte',#gte - greater than or equal to 
        label='Date From',
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    end_date = django_filters.DateFilter(
        field_name='date', 
        lookup_expr='lte',#lte - less than or equal to 
        label='Date To',
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    
    category = django_filters.ModelMultipleChoiceFilter(
        
        field_name='category',
        queryset = Category.objects.all(),
        widget = forms.CheckboxSelectMultiple()
    )
    class Meta:
        model = Transaction
        fields= ('transaction_type','start_date','end_date','category')