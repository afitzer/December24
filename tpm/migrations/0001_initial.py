# Generated by Django 5.1.4 on 2024-12-07 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TradeFund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAccountPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('plan_details', models.TextField()),
                ('trade_fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tpm.tradefund')),
            ],
        ),
        migrations.CreateModel(
            name='TradePromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('customer_account_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tpm.customeraccountplan')),
            ],
        ),
    ]
