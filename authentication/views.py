from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import reverse_lazy
from django.utils import timezone
from drf_yasg.generators import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class LoginAPIView(APIView):
    """
    APIログイン実装
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(description="ユーザー名", type=openapi.TYPE_STRING),
                "password": openapi.Schema(description="パスワード", type=openapi.TYPE_STRING),
            },
        ),
        responses={200: "OK", 400: "Bad Request"},
    )
    def post(self, request):
        """ログイン"""
        username = request.data.get("username")
        password = request.data.get("password")
        auth_user = authenticate(username=username, password=password)
        if auth_user is not None:
            login(request, auth_user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    """
    APIログアウト実装
    """

    def post(self, request):
        """ログアウト"""
        logout(request)
        return Response(status=status.HTTP_200_OK)


class PasswordReset(PasswordResetView):
    """
    パスワード再設定ページ
    """

    from_email = settings.DEFAULT_FROM_EMAIL
    success_url = reverse_lazy("auth:password_reset_done")


class PasswordResetDone(PasswordResetDoneView):
    """
    パスワード再設定確認ページ
    """
    pass


class PasswordResetConfirm(PasswordResetConfirmView):
    """
    新規パスワード入力ページ
    """
    pass


class PasswordResetComplete(PasswordResetCompleteView):
    """
    パスワード変更完了ページ
    """
    pass
