from django.urls import path
from rest_app.views import RegisterView,LoginView

app_name="restapp"

urlpatterns = [
    path('',RegisterView.as_view(),name='register'),
    path('login',LoginView.as_view(),name='login'),
    
]