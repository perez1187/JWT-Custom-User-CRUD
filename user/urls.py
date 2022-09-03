from django.urls import path

# local
from . import views

urlpatterns = [
    path('register/', views.RegisterApi.as_view(), name="register"),
    path('login/', views.LoginApi.as_view(), name="Login"),
    path('me/', views.UserApi.as_view(), name="me"),
    path('logout/', views.LogoutApi.as_view(), name="logout"),
]