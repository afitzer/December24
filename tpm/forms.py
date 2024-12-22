from django import forms
from .models import TradeFund, CustomerAccountPlan, WeeklySalesForecast


class TradeFundForm(forms.ModelForm):
    class Meta:
        model = TradeFund
        fields = ["name", "budget", "start_date", "end_date"]


class CustomerAccountPlanForm(forms.ModelForm):
    class Meta:
        model = CustomerAccountPlan
        fields = ["customer_name", "plan_details", "trade_fund"]


class WeeklySalesForecastForm(forms.ModelForm):
    class Meta:
        model = WeeklySalesForecast
        fields = ["week", "baseline", "adjustment"]


class TradePromotionFilterForm(forms.Form):
    customer_account_plan = forms.ModelChoiceField(
        queryset=CustomerAccountPlan.objects.all(),
        required=False,
        label="Customer Account Plan",
    )
