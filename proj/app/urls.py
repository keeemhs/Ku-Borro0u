from django.urls import path
from . import views

app_name = "kakaopay"

from .views import *
urlpatterns = [
    path('', MainpageView.as_view(), name='mainpage'),
    path('', views.index, name = "index"),
]
