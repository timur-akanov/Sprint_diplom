import pytest

from helpers.api_helpers import sign_in_user


@pytest.mark.api
class TestUserAuth:
    def test_sign_in_user(self, new_user):
        response = sign_in_user(new_user["client"], new_user["email"], new_user["password"])

        assert response.status_code in (200, 201), response.text
        payload = response.json()
        assert payload["user"]["email"] == new_user["email"]
        token = payload.get("token") or payload.get("access_token")
        assert token and token["access_token"]
