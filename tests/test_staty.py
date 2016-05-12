import pytest

from staty import HTTP_STATUS_CODES, Informational, Successful, Redirection


def test_class_names_and_messages():
    for status in HTTP_STATUS_CODES.values():
        message = status.message.replace(" ", "").replace("-", "").lower()
        assert status.__name__.lower() == message


@pytest.mark.parametrize("category_class,quantity", [
    (Informational, 3),
    (Successful, 10),
    (Redirection, 9)
])
def test_status_in_categories(category_class, quantity):
    statuses = [s for s in HTTP_STATUS_CODES.values() if issubclass(s, category_class)]
    assert len(statuses) == quantity
