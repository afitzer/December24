# Generated by Django 5.1.4 on 2024-12-08 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklySalesForecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.DateField()),
                ('volume_forecast', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_account_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tpm.customeraccountplan')),
            ],
        ),
    ]
