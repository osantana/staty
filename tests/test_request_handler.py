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

from staty import BadRequestException
from staty.handlers.requests import raise_for_status


def test_basic_response(ok_response):
    response = raise_for_status(ok_response)
    assert response == ok_response


# noinspection PyTypeChecker,PyShadowingNames
def test_error_response(bad_request_response):
    with pytest.raises(BadRequestException):
        raise_for_status(bad_request_response)
