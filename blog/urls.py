from django.urls import path
from .views import Home
from .views import Menu


# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

urlpatterns = [
        path('', Home),
        path('', Menu),
]
