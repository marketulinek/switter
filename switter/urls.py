from django.urls import path
from .views import dashboard


app_name='switter'

urlpatterns = [
    path('', dashboard, name='dashboard')
]