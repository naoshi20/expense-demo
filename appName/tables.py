import django_tables2 as tables
from .models import Expense

class ExpenseTable(tables.Table):
        class Meta:
                model = Expense
                template_name = "django_tables2/bootstrap.html"
                fields = ("title", "cost_indexes", "amount_of_money", "remarks", "created_at")
                attrs = {"class": "table table-striped"}