from tokenize import Expfloat
from django.shortcuts import render
from .models import Expensechecker,Balance

# Create your views here.
def home(request):
    return render(request,"expensechecker.html")

def addexpense(request):
  responseDic={}
  flag=0
  try:
    Expense=request.POST["expense"]
    Amount=int(request.POST["money"])
    expenselist=Expensechecker.objects.all()
    for i in expenselist:
         if Expense in i.expense:
           flag=1
    if flag==1:
      bal=Balance.objects.get(id=1)
      if Amount>bal.balance:
         responseDic["msg1"]="Insufficient balance" 
         return render(request,"expensechecker.html",responseDic)
      else:
               exp=Expensechecker.objects.get(expense=Expense)
               oldamt=exp.cost
               curramt=oldamt+Amount
               exp1=Expensechecker.objects.filter(expense=Expense)
               exp1.update(cost=curramt)
               bal=Balance.objects.get(id=1)
               bal.balance-=Amount
               bal.save()
               responseDic["msg1"]="Expense updated\n" 
               responseDic["dic1"]="Current balance is:"+str(bal.balance)
               return render(request,"expensechecker.html",responseDic)

    else:
             bal=Balance.objects.get(id=1)
             if Amount>bal.balance:
                responseDic["msg1"]="Insufficient balance" 
                return render(request,"expensechecker.html",responseDic)

             else:
              expenselist=Expensechecker.objects.all()
              bal.balance-=Amount
              bal.save()
              expenseobj=Expensechecker(expense=Expense,cost=Amount)
              expenseobj.save()
              responseDic["msg1"]="Expense added\n"
              responseDic["dic1"]="Current balance is:"+str(bal.balance)
              return render(request,"expensechecker.html",responseDic)

  except Exception as e:
     print(e)
     responseDic["msg1"]="Expense cannot be added."
     return render(request,"expensechecker.html",responseDic)

               
def addbalance(request):
  responseDic2={}
  try:
    Amount=int(request.POST["amount"])
    bal=Balance.objects.get(id=1)
    bal.balance+=Amount
    bal.save()
    responseDic2["dic2"]="Balance added."
    responseDic2["msg2"]="Current balance is:"+str(bal.balance)
    return render(request,"expensechecker.html",responseDic2)

  except Exception as e:
       print(e)
       responseDic2["dic1"]="Balance cannot be added"
       return render(request,"expensechecker.html",responseDic2)


def display(request):
   expenselist=Expensechecker.objects.all()
   return render(request,"expensechecker.html",{'emp':expenselist})