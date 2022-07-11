from django.urls import path
from .views import dashboard, profile_list, profile, login_as


app_name='switter'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login-as/', login_as, name='login_as'),
    path('profiles/', profile_list, name='profile_list'),
    path('profile/<int:pk>/', profile, name='profile')
]