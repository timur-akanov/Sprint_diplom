import pytest

from data.test_data import UPDATED_LISTING_DATA
from helpers.api_helpers import create_listing, register_user, update_listing
from helpers.email_generator import generate_email


@pytest.mark.api
class TestUpdateListing:
    def test_update_listing_by_owner(self, new_user):
        create_response = create_listing(new_user["client"], new_user["token"])
        listing_id = create_response.json()["id"]

        response = update_listing(new_user["client"], new_user["token"], listing_id)

        assert response.status_code == 200, response.text
        payload = response.json()
        assert payload["name"] == UPDATED_LISTING_DATA["name"]
        assert payload["condition"] == UPDATED_LISTING_DATA["condition"]
        assert payload["city"] == UPDATED_LISTING_DATA["city"]
        assert payload["description"] == UPDATED_LISTING_DATA["description"]
        assert payload["price"] == int(UPDATED_LISTING_DATA["price"])

    def test_cannot_update_other_users_listing(self, api_client):
        owner_email = generate_email()
        attacker_email = generate_email()

        owner_response, _, _ = register_user(api_client, email=owner_email)
        attacker_response, _, _ = register_user(api_client, email=attacker_email)

        owner_token = owner_response.json()["access_token"]["access_token"]
        attacker_token = attacker_response.json()["access_token"]["access_token"]

        create_response = create_listing(api_client, owner_token)
        listing_id = create_response.json()["id"]

        response = update_listing(api_client, attacker_token, listing_id)

        assert response.status_code == 401, response.text
        payload = response.json()
        assert "не найден или у вас нет прав" in payload["message"]
