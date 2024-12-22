from django import template
from django.template.defaultfilters import floatformat
from django.contrib.humanize.templatetags.humanize import intcomma
from tpm.models import WeeklySalesForecast

register = template.Library()


@register.filter
def currency(value):
    try:
        value = float(value)
    except (ValueError, TypeError):
        return value
    return "${}".format(intcomma(floatformat(value, 2)))


@register.filter
def get_forecast(forecasts, week, field):
    forecast = forecasts.filter(week=week).first()
    if forecast:
        return getattr(forecast, field)
    return None
