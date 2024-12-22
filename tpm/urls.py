from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("trade_funds/", views.trade_funds, name="trade_funds"),
    path(
        "customer_account_plans/",
        views.customer_account_plans,
        name="customer_account_plans",
    ),
    path(
        "customer_account_plans/<int:pk>/",
        views.customer_account_plan_detail,
        name="customer_account_plan_detail",
    ),
    path("create_trade_fund/", views.create_trade_fund, name="create_trade_fund"),
    path(
        "create_customer_account_plan/",
        views.create_customer_account_plan,
        name="create_customer_account_plan",
    ),
    path("trade_promotions/", views.trade_promotions, name="trade_promotions"),
]
