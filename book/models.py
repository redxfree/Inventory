from datetime import timedelta,datetime
from time import time
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

    
class Book(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    rent = models.IntegerField()
        
    def __str__(self):
        return '%s-%s-%s' %(str(self.name),str(self.category),str(self.rent))
    
class Rent(models.Model):
    daily_rent = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='price_for_day')
    
    def __Str__(self):
        return str(self.daily_rent) 
    

class Transaction(models.Model):
    book_name = models.ForeignKey(Book,on_delete=models.CASCADE)
    person_name = models.OneToOneField(User,on_delete=models.CASCADE)
    isuued_date = models.DateTimeField(default=datetime.now()+ timedelta(days=10))
    
        
class Return(models.Model):
    book_name = models.ForeignKey(Book,on_delete=models.CASCADE)
    person_name = models.OneToOneField(User,on_delete=models.CASCADE)   
    book_return = models.DateField(auto_now_add=True)
    total = models.ForeignKey(Book,on_delete=models.CASCADE)
    days = models.IntegerField()
    
    @property
    def total(self):
        total = self.total * self.days
        return total
    