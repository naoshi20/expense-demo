from django import forms
from .models import Expense


class ExpenseCreateForm(forms.ModelForm):
        class Meta:
                model = Expense
                fields = ('title', 'cost_indexes', 'amount_of_money', 'remarks')  #'__all__' ('summary', 'description', 'created_at')
        #inputタグにclass属性を付与する
        def __init__(self, *args, **kwargs):
                super(ExpenseCreateForm, self).__init__(*args, **kwargs)
                for i, visible in enumerate(self.visible_fields()):
                        visible.field.widget.attrs['class'] = 'form-control'
                        visible.field.widget.attrs['id'] = 'formGroupInput' + str(i)