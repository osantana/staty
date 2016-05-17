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


from . import base
from . import exceptions

HTTP_STATUS_CODES = {}
HTTP_ERROR_CODES = {}


def register(http_status_class):
    code = http_status_class.code

    if code in HTTP_STATUS_CODES:
        raise exceptions.RegistrationError("Status code is already registered")

    HTTP_STATUS_CODES[code] = http_status_class
    if issubclass(http_status_class, base.ErrorCodeMixin):
        HTTP_ERROR_CODES[code] = http_status_class


@register
class Continue(base.Informational, base.HTTP11Mixin):
    code = 100
    message = "Continue"


@register
class SwitchingProtocols(base.Informational, base.HTTP11Mixin):
    code = 101
    message = "Switching Protocols"


@register
class Processing(base.Informational, base.WebDAVMixin):
    code = 102
    message = "Processing"


@register
class Checkpoint(base.Informational, base.UnofficialMixin):
    code = 103
    message = "Checkpoint"
    reference = "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#Unofficial_codes"


@register
class Ok(base.Successful, base.HTTP10Mixin):
    code = 200
    message = "OK"


@register
class Created(base.Successful, base.HTTP10Mixin):
    code = 201
    message = "Created"


@register
class Accepted(base.Successful, base.HTTP10Mixin):
    code = 202
    message = "Accepted"


@register
class NonAuthoritativeInformation(base.Successful, base.HTTP11Mixin):
    code = 203
    message = "Non-Authoritative Information"


@register
class NoContent(base.Successful, base.HTTP10Mixin):
    code = 204
    message = "No Content"


@register
class ResetContent(base.Successful, base.HTTP11Mixin):
    code = 205
    message = "Reset Content"


@register
class PartialContent(base.Successful, base.HTTP11Mixin):
    code = 206
    message = "Partial Content"


@register
class MultiStatus(base.Successful, base.WebDAVMixin):
    code = 207
    message = "Multi-Status"


@register
class AlreadyReported(base.Successful, base.WebDAVMixin):
    code = 208
    message = "Already Reported"


@register
class IMUsed(base.Successful, base.HTTP11Mixin):
    code = 226
    message = "IM Used"


@register
class MultipleChoices(base.Redirection, base.HTTP10Mixin):
    code = 300
    message = "Multiple Choices"


@register
class MovedPermanently(base.Redirection, base.HTTP10Mixin):
    code = 301
    message = "Moved Permanently"


@register
class Found(base.Redirection, base.HTTP11Mixin):
    code = 302
    message = "Found"


@register
class SeeOther(base.Redirection, base.HTTP11Mixin):
    code = 303
    message = "See Other"


@register
class NotModified(base.Redirection, base.HTTP11Mixin):
    code = 304
    message = "Not Modified"


@register
class UseProxy(base.Redirection, base.HTTP11Mixin):
    code = 305
    message = "Use Proxy"


@register
class SwitchProxy(base.Redirection, base.HTTP11Mixin):
    code = 306
    message = "Switch Proxy"


@register
class TemporaryRedirect(base.Redirection, base.HTTP11Mixin):
    code = 307
    message = "Temporary Redirect"


@register
class PermanentRedirect(base.Redirection, base.HTTP11Mixin):
    code = 308
    message = "Permanent Redirect"


@register
class BadRequest(base.ClientError, base.HTTP10Mixin):
    code = 400
    message = "Bad Request"
    exception = exceptions.BadRequestException


@register
class Unauthorized(base.ClientError, base.HTTP10Mixin):
    code = 401
    message = "Unauthorized"
    exception = exceptions.UnauthorizedException


@register
class PaymentRequired(base.ClientError, base.HTTP10Mixin):
    code = 402
    message = "Payment Required"
    exception = exceptions.PaymentRequiredException


@register
class Forbidden(base.ClientError, base.HTTP10Mixin):
    code = 403
    message = "Forbidden"
    exception = exceptions.ForbiddenException


@register
class NotFound(base.ClientError, base.HTTP10Mixin):
    code = 404
    message = "Not Found"
    exception = exceptions.NotFoundException


@register
class MethodNotAllowed(base.ClientError, base.HTTP11Mixin):
    code = 405
    message = "Method Not Allowed"
    exception = exceptions.MethodNotAllowedException


@register
class NotAcceptable(base.ClientError, base.HTTP11Mixin):
    code = 406
    message = "Not Acceptable"
    exception = exceptions.NotAcceptableException


@register
class ProxyAuthenticationRequired(base.ClientError, base.HTTP11Mixin):
    code = 407
    message = "Proxy Authentication Required"
    exception = exceptions.ProxyAuthenticationRequiredException


@register
class RequestTimeout(base.ClientError, base.HTTP11Mixin):
    code = 408
    message = "Request Timeout"
    exception = exceptions.RequestTimeoutException


@register
class Conflict(base.ClientError, base.HTTP11Mixin):
    code = 409
    message = "Conflict"
    exception = exceptions.ConflictException


@register
class Gone(base.ClientError, base.HTTP11Mixin):
    code = 410
    message = "Gone"
    exception = exceptions.GoneException


@register
class LengthRequired(base.ClientError, base.HTTP11Mixin):
    code = 411
    message = "Length Required"
    exception = exceptions.LengthRequiredException


@register
class PreconditionFailed(base.ClientError, base.HTTP11Mixin):
    code = 412
    message = "Precondition Failed"
    exception = exceptions.PreconditionFailedException


@register
class PayloadTooLarge(base.ClientError, base.HTTP11Mixin):
    code = 413
    message = "Payload Too Large"
    exception = exceptions.PayloadTooLargeException


@register
class URITooLong(base.ClientError, base.HTTP11Mixin):
    code = 414
    message = "URI Too Long"
    exception = exceptions.URITooLongException


@register
class UnsupportedMediaType(base.ClientError, base.HTTP11Mixin):
    code = 415
    message = "Unsupported Media Type"
    exception = exceptions.UnsupportedMediaTypeException


@register
class RangeNotSatisfiable(base.ClientError, base.HTTP11Mixin):
    code = 416
    message = "Range Not Satisfiable"
    exception = exceptions.RangeNotSatisfiableException


@register
class ExpectationFailed(base.ClientError, base.HTTP11Mixin):
    code = 417
    message = "Expectation Failed"
    exception = exceptions.ExpectationFailedException


@register
class IAmATeapot(base.ClientError, base.HTCPCP10Mixin):
    code = 418
    message = "I am a teapot"
    exception = exceptions.IAmATeapotException


@register
class MethodFailure(base.ClientError, base.UnofficialMixin):
    code = 420
    message = "Method Failure"
    exception = exceptions.MethodFailureException
    reference = "Spring Framework"


@register
class MisdirectedRequest(base.ClientError, base.HTTP20Mixin):
    code = 421
    message = "Misdirected Request"
    exception = exceptions.MisdirectedRequestException


@register
class UnprocessableEntity(base.ClientError, base.WebDAVMixin):
    code = 422
    message = "Unprocessable Entity"
    exception = exceptions.UnprocessableEntityException


@register
class Locked(base.ClientError, base.WebDAVMixin):
    code = 423
    message = "Locked"
    exception = exceptions.LockedException


@register
class FailedDependency(base.ClientError, base.WebDAVMixin):
    code = 424
    message = "Failed Dependency"
    exception = exceptions.FailedDependencyException


@register
class UpgradeRequired(base.ClientError, base.HTTP11Mixin):
    code = 426
    message = "Upgrade Required"
    exception = exceptions.UpgradeRequiredException


@register
class PreconditionRequired(base.ClientError, base.HTTP11Mixin):
    code = 428
    message = "Precondition Required"
    exception = exceptions.PreconditionRequiredException


@register
class TooManyRequests(base.ClientError, base.HTTP11Mixin):
    code = 429
    message = "Too Many Requests"
    exception = exceptions.TooManyRequestsException


@register
class RequestHeaderFieldsTooLarge(base.ClientError, base.HTTP11Mixin):
    code = 431
    message = "Request Header Fields Too Large"
    exception = exceptions.RequestHeaderFieldsTooLargeException


@register
class LoginTimeout(base.ClientError, base.IISMixin):
    code = 440
    message = "Login Timeout"
    exception = exceptions.LoginTimeoutException


@register
class NoResponse(base.ClientError, base.NginxMixin):
    code = 444
    message = "No Response"
    exception = exceptions.NoResponseException


@register
class RetryWith(base.ClientError, base.IISMixin):
    code = 449
    message = "Retry With"
    exception = exceptions.RetryWithException


@register
class BlockedByWindowsParentalControls(base.ClientError, base.UnofficialMixin):
    code = 450
    message = "Blocked By Windows Parental Controls"
    reference = "Microsoft"
    exception = exceptions.BlockedByWindowsParentalControlsException


@register
class UnavailableForLegalReasons(base.ClientError, base.HTTP11Mixin):
    code = 451
    message = "Unavailable For Legal Reasons"
    exception = exceptions.UnavailableForLegalReasonsException


class Redirect(base.ClientError, base.IISMixin):
    code = 451
    message = "Redirect"
    exception = exceptions.BadGatewayException


@register
class SSLCertificateError(base.ClientError, base.NginxMixin):
    code = 495
    message = "SSL Certificate Error"
    exception = exceptions.SSLCertificateErrorException


@register
class SSLCertificateRequired(base.ClientError, base.NginxMixin):
    code = 496
    message = "SSL Certificate Required"
    exception = exceptions.SSLCertificateRequiredException


@register
class HTTPRequestSentToHTTPSPort(base.ClientError, base.NginxMixin):
    code = 497
    message = "HTTP Request Sent To HTTPS Port"
    exception = exceptions.HTTPRequestSentToHTTPSPortException


@register
class InvalidToken(base.ClientError, base.UnofficialMixin):
    code = 498
    message = "Invalid Token"
    reference = "ArcGIS for Server"
    exception = exceptions.InvalidTokenException


@register
class ClientClosedRequest(base.ClientError, base.NginxMixin):
    code = 499
    message = "Client Closed Request"
    exception = exceptions.ClientClosedRequestException


class RequestHasBeenForbiddenByAntivirus(base.ClientError, base.UnofficialMixin):
    code = 499
    message = "Request Has Been Forbidden By Antivirus"
    reference = "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#Unofficial_codes"
    exception = exceptions.RequestHasBeenForbiddenByAntivirusException


class TokenRequired(base.ClientError, base.UnofficialMixin):
    code = 499
    message = "Token Required"
    reference = "ArcGIS for Server"
    exception = exceptions.TokenRequiredException


@register
class InternalServerError(base.ServerError, base.HTTP10Mixin):
    code = 500
    message = "Internal Server Error"
    exception = exceptions.InternalServerErrorException


# noinspection PyShadowingBuiltins
@register
class NotImplemented(base.ServerError, base.HTTP10Mixin):
    code = 501
    message = "Not Implemented"
    exception = exceptions.NotImplementedException


@register
class BadGateway(base.ServerError, base.HTTP10Mixin):
    code = 502
    message = "Bad Gateway"
    exception = exceptions.BadGatewayException


@register
class ServiceUnavailable(base.ServerError, base.HTTP10Mixin):
    code = 503
    message = "Service Unavailable"
    exception = exceptions.ServiceUnavailableException


@register
class GatewayTimeout(base.ServerError, base.HTTP11Mixin):
    code = 504
    message = "Gateway Timeout"
    exception = exceptions.GatewayTimeoutException


@register
class HTTPVersionNotSupported(base.ServerError, base.HTTP11Mixin):
    code = 505
    message = "HTTP Version Not Supported"
    exception = exceptions.HTTPVersionNotSupportedException


@register
class VariantAlsoNegotiates(base.ServerError, base.HTTP11Mixin):
    code = 506
    message = "Variant Also Negotiates"
    exception = exceptions.VariantAlsoNegotiatesException


@register
class InsufficientStorage(base.ServerError, base.WebDAVMixin):
    code = 507
    message = "Insufficient Storage"
    exception = exceptions.InsufficientStorageException


@register
class LoopDetected(base.ServerError, base.WebDAVMixin):
    code = 508
    message = "Loop Detected"
    exception = exceptions.LoopDetectedException


class BandwidthLimitExceeded(base.ServerError, base.UnofficialMixin):
    code = 509
    message = "Bandwidth Limit Exceeded"
    reference = "Apache Web Server/cPanel"
    exception = exceptions.BandwidthLimitExceededException


@register
class NotExtended(base.ServerError, base.HTTP11Mixin):
    code = 510
    message = "Not Extended"
    exception = exceptions.NotExtendedException


@register
class NetworkAuthenticationRequired(base.ServerError, base.HTTP11Mixin):
    code = 511
    message = "Network Authentication Required"
    exception = exceptions.NetworkAuthenticationRequiredException


@register
class UnknownError(base.ServerError, base.CloudflareMixin):
    code = 520
    message = "Unknown Error"
    exception = exceptions.UnknownErrorException


@register
class WebServerIsDown(base.ServerError, base.CloudflareMixin):
    code = 521
    message = "Web Server Is Down"
    exception = exceptions.WebServerIsDownException


@register
class ConnectionTimedOut(base.ServerError, base.CloudflareMixin):
    code = 522
    message = "Connection Timed Out"
    exception = exceptions.ConnectionTimedOutException


@register
class OriginIsUnreachable(base.ServerError, base.CloudflareMixin):
    code = 523
    message = "Origin Is Unreachable"
    exception = exceptions.OriginIsUnreachableException


@register
class ATimeoutOccurred(base.ServerError, base.CloudflareMixin):
    code = 524
    message = "A Timeout Occurred"
    exception = exceptions.ATimeoutOccurredException


@register
class SSLHandshakeFailed(base.ServerError, base.CloudflareMixin):
    code = 525
    message = "SSL Handshake Failed"
    exception = exceptions.SSLHandshakeFailedException


@register
class InvalidSSLCertificate(base.ServerError, base.CloudflareMixin):
    code = 526
    message = "Invalid SSL Certificate"
    exception = exceptions.InvalidSSLCertificateException


@register
class SiteIsFrozen(base.ServerError, base.UnofficialMixin):
    code = 530
    message = "Site Is Frozen"
    reference = "Pantheon"
    exception = exceptions.SiteIsFrozenException
