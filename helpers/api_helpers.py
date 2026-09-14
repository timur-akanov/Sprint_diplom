from data.test_data import (
    BASE_URL,
    DEFAULT_PASSWORD,
    LISTING_DATA,
    LISTING_FILES,
    UPDATED_LISTING_DATA,
)
from helpers.email_generator import generate_email


def register_user(client, email=None, password=DEFAULT_PASSWORD):
    email = email or generate_email()
    response = client.post(
        f"{BASE_URL}/signup",
        json={"email": email, "password": password},
        timeout=30,
    )
    return response, email, password


def sign_in_user(client, email, password):
    return client.post(
        f"{BASE_URL}/signin",
        json={"email": email, "password": password},
        timeout=30,
    )


def create_listing(client, token, payload=None, files=None):
    return client.post(
        f"{BASE_URL}/create-listing",
        data=payload or LISTING_DATA,
        files=files or LISTING_FILES,
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )


def update_listing(client, token, listing_id, payload=None, files=None):
    return client.patch(
        f"{BASE_URL}/update-offer/{listing_id}",
        data=payload or UPDATED_LISTING_DATA,
        files=files or LISTING_FILES,
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )


def delete_listing(client, token, listing_id):
    return client.delete(
        f"{BASE_URL}/listings/{listing_id}",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
