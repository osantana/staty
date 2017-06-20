import pytest
from requests import Response

from staty import Ok, BadRequest


@pytest.fixture
def response():
    return Response()


@pytest.fixture
def ok_response(response):
    response.status_code = Ok.code
    response.reason = Ok.message
    return response


@pytest.fixture
def bad_request_response(response):
    response.status_code = BadRequest.code
    response.reason = BadRequest.message
    return response
