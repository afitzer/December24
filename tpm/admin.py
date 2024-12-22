from django.contrib import admin
from .models import TradeFund, CustomerAccountPlan, TradePromotion, WeeklySalesForecast


@admin.register(TradeFund)
class TradeFundAdmin(admin.ModelAdmin):
    list_display = ("name", "budget", "start_date", "end_date", "remaining_budget")


@admin.register(CustomerAccountPlan)
class CustomerAccountPlanAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "plan_details", "trade_fund")


@admin.register(TradePromotion)
class TradePromotionAdmin(admin.ModelAdmin):
    list_display = (
        "promotion_name",
        "description",
        "start_date",
        "end_date",
        "customer_account_plan",
    )


@admin.register(WeeklySalesForecast)
class WeeklySalesForecastAdmin(admin.ModelAdmin):
    list_display = ("customer_account_plan", "week", "baseline", "adjustment", "total_adjusted_forecast")
