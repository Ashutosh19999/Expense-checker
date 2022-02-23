from django.db import models

# Create your models here.
class Expensechecker(models.Model):
    expense=models.CharField(max_length=30)
    cost=models.IntegerField()
    def __str__(self):
        return self.expense

class Balance(models.Model):
    balance=models.BigIntegerField()
    def __str__(self):
        return self.balance 

