from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from users.factory import AppUserFactory


class LoginTest(APITestCase):
    """
    ログインテスト
    """

    url = "/api/login/"

    def setUp(self) -> None:
        self.user = AppUserFactory()

        # パスワードをpasswordに
        users = get_user_model().objects.all()
        for user in users:
            user.set_password("password")
            user.save()

    def test_post(self):
        payload = {"username": self.user.auth_user.username, "password": "wrongpassword"}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, 400)

        payload = {"username": self.user.auth_user.username, "password": "password"}

        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, 200)
