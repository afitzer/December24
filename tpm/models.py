from django.db import models
from datetime import date, timedelta


class TradeFund(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    @property
    def remaining_budget(self):
        # Assuming you have a way to calculate the spent amount
        spent_amount = 0  # Replace with actual calculation
        return self.budget - spent_amount


class CustomerAccountPlan(models.Model):
    customer_name = models.CharField(max_length=100)
    plan_details = models.TextField()
    trade_fund = models.ForeignKey(TradeFund, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name


class TradePromotion(models.Model):
    promotion_name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    customer_account_plan = models.ForeignKey(
        CustomerAccountPlan, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.promotion_name


class WeeklySalesForecast(models.Model):
    customer_account_plan = models.ForeignKey(
        CustomerAccountPlan, on_delete=models.CASCADE
    )
    week = models.DateField()
    baseline = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_adjusted_forecast = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, editable=False
    )

    def save(self, *args, **kwargs):
        self.baseline = self.baseline or 0.00
        self.adjustment = self.adjustment or 0.00
        self.total_adjusted_forecast = self.baseline + self.adjustment
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_account_plan.customer_name} - {self.week}"
