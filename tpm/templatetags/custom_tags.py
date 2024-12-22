from django import template
from tpm.models import WeeklySalesForecast

register = template.Library()


@register.simple_tag
def get_forecast(forecasts, week, field):
    forecast = forecasts.filter(week=week).first()
    if forecast:
        return getattr(forecast, field)
    return None
