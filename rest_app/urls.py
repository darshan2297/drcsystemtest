from django.urls import path
from rest_app.views import RegisterView,LoginView,OTPView,HomeView,EmailPrimary

app_name="restapp"

urlpatterns = [
    path('',RegisterView.as_view(),name='register'),
    path('login',LoginView.as_view(),name='login'),
    path('otpview',OTPView.as_view(),name='otpview'),
    path('home',HomeView.as_view(),name='home'),
    path('primary/<int:pk>',EmailPrimary.as_view(),name='primary'),
]