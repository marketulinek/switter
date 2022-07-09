from django.urls import path
from .views import dashboard, profile_list, profile


app_name='switter'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profiles/', profile_list, name='profile_list'),
    path('profile/<int:pk>/', profile, name='profile')
]