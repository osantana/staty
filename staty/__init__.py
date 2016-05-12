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


from . import exceptions

HTTP_STATUS_CODES = {}


def register(http_status_class):
    HTTP_STATUS_CODES[http_status_class.code] = http_status_class


class HTTP10Mixin(object):
    rfcs = 1945


class HTTP11aMixin(object):
    rfcs = 1945, 2068, 2616, 2817, 5785, 6266, 6585


class HTTP11bMixin(object):
    rfcs = HTTP11aMixin.rfcs + (7230, 7231, 7232, 7233, 7234, 7235, 7236, 7237, 7238, 7239, 7240)


class WebDAVMixin(object):
    rfcs = HTTP11bMixin.rfcs + (2518, 4918, 5689)


class AbstractStatus(object):
    code = None
    message = ""
    category_code = ""
    category_name = ""
    exception = None


class Informational(AbstractStatus):
    category_code = "1xx"
    category_name = "Informational"


class Successful(AbstractStatus):
    category_code = "2xx"
    category_name = "Successful"


class Redirection(AbstractStatus):
    category_code = "3xx"
    category_name = "Redirection"


@register
class Continue(Informational, HTTP11bMixin):
    code = 100
    message = "Continue"


@register
class SwitchingProtocols(Informational, HTTP11bMixin):
    code = 101
    message = "Switching Protocols"


@register
class Processing(Informational, WebDAVMixin):
    code = 102
    message = "Processing"


@register
class Ok(Successful, HTTP10Mixin):
    code = 200
    message = "OK"


@register
class Created(Successful, HTTP10Mixin):
    code = 201
    message = "Created"


@register
class Accepted(Successful, HTTP10Mixin):
    code = 202
    message = "Accepted"


@register
class NonAuthoritativeInformation(Successful, HTTP11bMixin):
    code = 203
    message = "Non-Authoritative Information"


@register
class NoContent(Successful, HTTP10Mixin):
    code = 204
    message = "No Content"


@register
class ResetContent(Successful, HTTP11bMixin):
    code = 205
    message = "Reset Content"


@register
class PartialContent(Successful, HTTP11bMixin):
    code = 206
    message = "Partial Content"


@register
class MultiStatus(Successful, WebDAVMixin):
    code = 207
    message = "Multi-Status"


@register
class AlreadyReported(Successful, WebDAVMixin):
    code = 208
    message = "Already Reported"
    rfcs = WebDAVMixin.rfcs + (5842,)


@register
class IMUsed(Successful, HTTP11bMixin):
    code = 226
    message = "IM Used"
    rfcs = HTTP11bMixin.rfcs + (3229,)


@register
class MultipleChoices(Redirection, HTTP10Mixin):
    code = 300
    message = "Multiple Choices"


@register
class MovedPermanently(Redirection, HTTP10Mixin):
    code = 301
    message = "Moved Permanently"


@register
class Found(Redirection, HTTP11bMixin):
    code = 302
    message = "Found"


@register
class SeeOther(Redirection, HTTP11bMixin):
    code = 303
    message = "See Other"


@register
class NotModified(Redirection, HTTP11bMixin):
    code = 304
    message = "Not Modified"


@register
class UseProxy(Redirection, HTTP11aMixin):
    code = 305
    message = "Use Proxy"


@register
class SwitchProxy(Redirection, HTTP11aMixin):
    code = 306
    message = "Switch Proxy"


@register
class TemporaryRedirect(Redirection, HTTP11aMixin):
    code = 307
    message = "Temporary Redirect"


@register
class PermanentRedirect(Redirection, HTTP11bMixin):
    code = 308
    message = "Permanent Redirect"
    rfcs = HTTP11bMixin.rfcs + (7538,)


