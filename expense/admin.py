from django.contrib import admin
from .models import Expensechecker,Balance

# Register your models here.
class ExpensecheckerAdmin(admin.ModelAdmin):
    list_display=('expense','cost')
    ordering=('expense',)
    search_fields=('expense','cost')
admin.site.register(Expensechecker,ExpensecheckerAdmin)

class BalanceAdmin(admin.ModelAdmin):
    list_display=('balance',)
admin.site.register(Balance,BalanceAdmin)