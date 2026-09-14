import pytest

from helpers.api_helpers import register_user
from helpers.email_generator import generate_email


@pytest.mark.api
class TestUserRegistration:
    def test_register_user(self, api_client):
        email = generate_email()

        response, _, _ = register_user(api_client, email=email)

        assert response.status_code == 201, response.text
        payload = response.json()
        assert payload["user"]["email"] == email
        assert "access_token" in payload
        assert payload["access_token"]["access_token"]

    def test_register_user_duplicate_email(self, api_client):
        email = generate_email()

        first_response, _, _ = register_user(api_client, email=email)
        assert first_response.status_code == 201, first_response.text

        second_response, _, _ = register_user(api_client, email=email)

        assert second_response.status_code == 400, second_response.text
        payload = second_response.json()
        assert payload["message"] == "Почта уже используется"
