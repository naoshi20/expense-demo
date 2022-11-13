from django.utils import timezone 
from django import forms
from django.db import models

class Expense(models.Model):
        title = models.CharField('タイトル', max_length=50)
        cost_indexes = models.CharField('項目', max_length=50)
        amount_of_money = models.IntegerField('金額')
        remarks = models.TextField('備考', blank=True)
        receipt = models.ImageField('画像', upload_to='static/images',blank=True, null=True)
        created_at = models.DateTimeField('作成日', default=timezone.now)
        
        def __str__(self):
                return self.title