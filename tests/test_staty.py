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

from staty import InternalServerError, Ok, base, exceptions, status, BadRequest


def test_class_names_and_messages():
    for st in status.codes.values():
        message = st.message.replace(" ", "").replace("-", "").lower()
        assert st.__class__.__name__.lower() == message


@pytest.mark.parametrize("category_class,quantity", [
    (base.Informational, 4),
    (base.Successful, 10),
    (base.Redirection, 9),
    (base.ClientError, 38),
    (base.ServerError, 19),
])
def test_status_in_categories(category_class, quantity):
    statuses = [s for s in status.codes.values() if isinstance(s, category_class)]
    assert len(statuses) == quantity


def test_status_instance():
    ok = Ok()
    assert str(ok) == "200 OK"
    assert ok == 200


def test_exception_class_names():
    for http_status in status.codes.values():
        if not hasattr(http_status, "exception"):
            continue

        assert "{}Exception".format(http_status.__class__.__name__) == http_status.exception.__name__


def test_exception_response_argument():
    try:
        raise exceptions.HTTPError(response="response")
    except exceptions.HTTPError as exc:
        assert exc.response == "response"


def test_exception_request_argument():
    try:
        raise exceptions.HTTPError(request="request")
    except exceptions.HTTPError as exc:
        assert exc.request == "request"


def test_exception_response_request_argument():
    class FakeResponse:
        request = "request"

    fake_response = FakeResponse()

    try:
        raise exceptions.HTTPError(response=fake_response)
    except exceptions.HTTPError as exc:
        assert exc.response == fake_response
        assert exc.request == "request"


def test_register_class():
    class DummyClass:
        code = 999
        message = "Dummy Class"

    registered = status.register(DummyClass)
    assert registered == DummyClass


def test_cannot_register_twice():
    class DummyClass(object):
        code = 100  # Status code 100 is already registered

    with pytest.raises(exceptions.RegistrationException):
        status.register(DummyClass)


def test_registered_attributes_in_status_map():
    assert status.HTTP_200_OK == 200
    assert status.HTTP_400_BAD_REQUEST == BadRequest()
    assert status.HTTP_404_NOT_FOUND == "not found"
    assert status.HTTP_500_INTERNAL_SERVER_ERROR == InternalServerError
    assert status.HTTP_304_NOT_MODIFIED == status.HTTP_304_NOT_MODIFIED

    assert status[200] == 200
    assert status[400] == BadRequest()
    assert status[404] == "not found"
    assert status[500] == InternalServerError
    assert status[304] == status.HTTP_304_NOT_MODIFIED

    assert status[200] != []
    assert status[200] != ["invalid comparison"]
