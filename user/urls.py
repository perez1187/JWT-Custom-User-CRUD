from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegisterApi.as_view(), name="Register"),
    path('login/', views.LoginApi.as_view(), name="Login"),
    path('me/', views.UserApi.as_view(), name="me"),
]