# Generated by Django 5.1.4 on 2024-12-08 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpm', '0002_weeklysalesforecast'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklysalesforecast',
            old_name='volume_forecast',
            new_name='adjustment',
        ),
        migrations.AddField(
            model_name='weeklysalesforecast',
            name='baseline',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weeklysalesforecast',
            name='total_adjusted_forecast',
            field=models.DecimalField(decimal_places=2, default=2, editable=False, max_digits=10),
            preserve_default=False,
        ),
    ]
