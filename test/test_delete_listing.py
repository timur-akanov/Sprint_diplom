import pytest

from helpers.api_helpers import create_listing, delete_listing


@pytest.mark.api
class TestDeleteListing:
    def test_delete_listing(self, new_user):
        create_response = create_listing(new_user["client"], new_user["token"])
        listing_id = create_response.json()["id"]

        response = delete_listing(new_user["client"], new_user["token"], listing_id)

        assert response.status_code == 200, response.text
        payload = response.json()
        assert "Объявление удалено успешно" in payload["message"]
