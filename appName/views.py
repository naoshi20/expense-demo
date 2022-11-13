from django.views.generic import TemplateView
from django.views import generic
from .forms import ExpenseCreateForm
from .models import Expense
from django.urls import reverse_lazy
class IndexView(generic.CreateView):
    model = Expense
    form_class = ExpenseCreateForm
    success_url = reverse_lazy('appName:index')