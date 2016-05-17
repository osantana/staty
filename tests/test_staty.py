# Copyright 2016 Osvaldo Santana Neto <staty@osantana.me>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pytest

from staty import HTTP_STATUS_CODES
from staty import register
from staty import base
from staty import exceptions


def test_class_names_and_messages():
    for status in HTTP_STATUS_CODES.values():
        message = status.message.replace(" ", "").replace("-", "").lower()
        assert status.__name__.lower() == message


@pytest.mark.parametrize("category_class,quantity", [
    (base.Informational, 4),
    (base.Successful, 10),
    (base.Redirection, 9),
    (base.ClientError, 38),
    (base.ServerError, 19),
])
def test_status_in_categories(category_class, quantity):
    statuses = [s for s in HTTP_STATUS_CODES.values() if issubclass(s, category_class)]
    assert len(statuses) == quantity


def test_exception_class_names():
    for http_status in HTTP_STATUS_CODES.values():
        if not hasattr(http_status, "exception"):
            continue

        assert "{}Exception".format(http_status.__name__) == http_status.exception.__name__


def test_exception_response_argument():
    try:
        raise exceptions.HTTPError("response")
    except exceptions.HTTPError as exc:
        assert exc.response == "response"


def test_cannot_register_twice():
    class DummyClass(object):
        code = 100  # Status code 100 is already registered

    with pytest.raises(exceptions.RegistrationError):
        register(DummyClass)
