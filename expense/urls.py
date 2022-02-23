from django.urls import path
from .import views

urlpatterns=[
    path('expense/',views.home),
    path('expense/addexpense',views.addexpense),
    path('expense/addbalance',views.addbalance),
    path('expense/displayexpense',views.display)
]