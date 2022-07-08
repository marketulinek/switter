from django.urls import path
from .views import dashboard, profile_list


app_name='switter'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile-list/', profile_list, name='profile_list')
]