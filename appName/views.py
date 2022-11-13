from django.views.generic import TemplateView
from django.views import generic
from .forms import ExpenseCreateForm
from .models import Expense
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
from .tables import ExpenseTable
from django_tables2.export.views import ExportMixin

class IndexView(ExportMixin, SingleTableView):
    model = Expense
    table_class = ExpenseTable
    template_name = 'appName/index.html'

class AddView(generic.CreateView):
    model = Expense
    form_class = ExpenseCreateForm
    success_url = reverse_lazy('appName:index')