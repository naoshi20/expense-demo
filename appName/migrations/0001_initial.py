# Generated by Django 3.2.16 on 2022-11-13 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('cost_indexes', models.CharField(max_length=50, verbose_name='項目')),
                ('amount_of_money', models.IntegerField(verbose_name='金額')),
                ('remarks', models.TextField(blank=True, verbose_name='備考')),
                ('date', models.DateField(verbose_name='日付')),
                ('receipt', models.ImageField(blank=True, null=True, upload_to='static/images', verbose_name='画像')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
    ]