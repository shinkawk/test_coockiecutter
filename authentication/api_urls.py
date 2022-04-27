from django.urls import path
from authentication import views

app_name = "auth-api"
urlpatterns = [
    path("login/", views.LoginAPIView.as_view()),
    path("logout/", views.LogoutAPIView.as_view()),
]
