# Generated by Django 5.1.4 on 2024-12-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpm', '0003_rename_volume_forecast_weeklysalesforecast_adjustment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklysalesforecast',
            name='adjustment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='weeklysalesforecast',
            name='baseline',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='weeklysalesforecast',
            name='total_adjusted_forecast',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10),
        ),
    ]