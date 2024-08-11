'''
how to generate fake data in django
'''


import random
from faker import Faker
from django.core.management.base import BaseCommand
from tracker.models import Transaction, User, Category

class Command(BaseCommand):
    help = "Generates transactions for testing"
    
    def handle(self, *args,**options):
        fake = Faker()
        
        # create categories 
        categories = ["Bills", "Food", "Clothes", "Medicals", "Housing", "Salary", "Socials", "Transport", "Vacations" ]
        # this one will create a category if not found in categories
        for category in categories:
            Category.objects.get_or_create(name=category)
            
        # get the user after categories filter is used to 
        user = User.objects.filter(username="aryan").first()
        # if user not found it will create the user and password will be stored in hash format not plane text format for security 
        if not user:
            user = User.objects.create_superuser(username="aryan dixit", password="test")
            
            
        # to combiner all the categories we created 
        categories= Category.objects.all()
        types = [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]
        for i in range(20):
            Transaction.objects.create(
                  Category = random.choice(categories),
                  user = user,  
                  amount = random.uniform(100,8000), # random floating no
                  date = fake.date_between(start_date='-1y',end_date='today'), # it will create something in past year
                  type = random.choice(types)
            )