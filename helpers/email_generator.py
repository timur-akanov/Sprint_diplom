from uuid import uuid4


def generate_email() -> str:
    return f"qa{uuid4().hex[:8]}@mail.ru"
