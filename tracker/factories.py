import factory 
from  tracker.models import Category, Transaction, User
from datetime import datetime

''' 
this module allow us to generate fake data
helps us to replace fexture in django   
fexture are json-static file which are hard to maintain

'''

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('username',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    # it will make username from word a 
    username = factory.Sequence(lambda a: 'user%d' % a )
    
    
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('name',)
    
    name = factory.Iterator(
        ["Bills", "Housing", "Salary", "Food", "Social"]
    )
    
class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction
        
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    amount = 500
    date = factory.Faker(
        'date_between',
        start_date = datetime(year=2022, month=1, day=1).date(),
        end_date = datetime.now().date()
    )
    
    type = factory.Iterator(
        [
            x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES
        ]
    )
    
    
    
    
    