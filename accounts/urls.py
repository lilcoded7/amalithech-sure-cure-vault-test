from accounts.views import CreatUserVaultAccountAPIView, LoginAccountAPIView
from django.urls import path

urlpatterns = [
    path("register/", CreatUserVaultAccountAPIView.as_view(), name="create_account"),
    path("login/", LoginAccountAPIView.as_view(), name="login"),
]
