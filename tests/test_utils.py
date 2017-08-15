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

from staty.utils import camel2snake


@pytest.mark.parametrize("camel,snake", [
    ('CamelCase', 'camel_case'),
    ('XYZCamelCase', 'xyz_camel_case'),
    ('xyzCamelCase', 'xyz_camel_case'),
    ('Camel123Case', 'camel123_case'),
    ('CamelCaseXYZ', 'camel_case_xyz'),
])
def test_camel_to_snake_case_lower(camel, snake):
    assert camel2snake(camel) == snake


@pytest.mark.parametrize("camel,snake", [
    ('CamelCase', 'CAMEL_CASE'),
    ('XYZCamelCase', 'XYZ_CAMEL_CASE'),
    ('xyzCamelCase', 'XYZ_CAMEL_CASE'),
    ('Camel123Case', 'CAMEL123_CASE'),
    ('CamelCaseXYZ', 'CAMEL_CASE_XYZ'),
])
def test_camel_to_snake_case_upper(camel, snake):
    assert camel2snake(camel, upper=True) == snake
