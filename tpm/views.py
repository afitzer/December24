from django.shortcuts import render, redirect, get_object_or_404
from .models import TradeFund, CustomerAccountPlan, TradePromotion, WeeklySalesForecast
from .forms import TradeFundForm, CustomerAccountPlanForm, WeeklySalesForecastForm, TradePromotionFilterForm
from datetime import date, timedelta
from decimal import Decimal


def index(request):
    trade_funds = TradeFund.objects.all()
    customer_account_plans = CustomerAccountPlan.objects.all()
    trade_promotions = TradePromotion.objects.all()
    context = {
        "trade_funds": trade_funds,
        "customer_account_plans": customer_account_plans,
        "trade_promotions": trade_promotions,
    }
    return render(request, "tpm/index.html", context)


def trade_funds(request):
    trade_funds = TradeFund.objects.all()
    context = {
        "trade_funds": trade_funds,
    }
    return render(request, "tpm/trade_funds.html", context)


def customer_account_plans(request):
    plans = CustomerAccountPlan.objects.all()
    context = {
        "plans": plans,
    }
    return render(request, "tpm/customer_account_plans.html", context)


def customer_account_plan_detail(request, pk):
    plan = get_object_or_404(CustomerAccountPlan, pk=pk)
    forecasts = WeeklySalesForecast.objects.filter(customer_account_plan=plan)
    weeks = [date(2025, 1, 1) + timedelta(weeks=i) for i in range(52)]
    if request.method == "POST":
        for week in weeks:
            baseline = Decimal(request.POST.get(f"baseline_{week}", 0.00))
            adjustment = Decimal(request.POST.get(f"adjustment_{week}", 0.00))
            forecast, created = WeeklySalesForecast.objects.get_or_create(
                customer_account_plan=plan,
                week=week,
                defaults={"baseline": baseline, "adjustment": adjustment},
            )
            if not created:
                forecast.baseline = baseline
                forecast.adjustment = adjustment
                forecast.save()
        return redirect("customer_account_plan_detail", pk=pk)
    context = {
        "plan": plan,
        "forecasts": forecasts,
        "weeks": weeks,
    }
    return render(request, "tpm/customer_account_plan_detail.html", context)


def create_trade_fund(request):
    if request.method == "POST":
        form = TradeFundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("trade_funds")
    else:
        form = TradeFundForm()
    return render(request, "tpm/create_trade_fund.html", {"form": form})


def create_customer_account_plan(request):
    if request.method == "POST":
        form = CustomerAccountPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_account_plans")
    else:
        form = CustomerAccountPlanForm()
    return render(request, "tpm/create_customer_account_plan.html", {"form": form})


def trade_promotions(request):
    form = TradePromotionFilterForm(request.GET or None)
    promotions = TradePromotion.objects.all()
    if form.is_valid():
        customer_account_plan = form.cleaned_data.get("customer_account_plan")
        if customer_account_plan:
            promotions = promotions.filter(customer_account_plan=customer_account_plan)
    context = {
        "form": form,
        "promotions": promotions,
    }
    return render(request, "tpm/trade_promotions.html", context)
