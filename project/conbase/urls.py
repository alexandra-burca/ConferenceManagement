import dashboard as dashboard
from django.urls import path
from . import views

app_name = 'conbase'

urlpatterns = [
    path('', views.dashboard, name="dashboard"),


]