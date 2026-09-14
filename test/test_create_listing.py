import pytest

from data.test_data import LISTING_DATA
from helpers.api_helpers import create_listing


@pytest.mark.api
class TestCreateListing:
    def test_create_listing(self, new_user):
        response = create_listing(new_user["client"], new_user["token"])

        assert response.status_code == 201, response.text
        payload = response.json()
        assert payload["name"] == LISTING_DATA["name"]
        assert payload["category"] == LISTING_DATA["category"]
        assert payload["condition"] == LISTING_DATA["condition"]
        assert payload["city"] == LISTING_DATA["city"]
        assert payload["price"] == int(LISTING_DATA["price"])
        assert payload["owner"] == new_user["user"]["id"]
