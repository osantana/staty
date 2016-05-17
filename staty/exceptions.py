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


class RecoverableErrorMixin(object):
    pass


class UnrecoverableErrorMixin(object):
    pass


class StatyBaseException(Exception):
    pass


class RegistrationError(StatyBaseException):
    pass


class HTTPError(StatyBaseException):
    def __init__(self, response=None):
        self.response = response


class ClientErrorException(HTTPError, UnrecoverableErrorMixin):
    pass


class ServerErrorException(HTTPError, RecoverableErrorMixin):
    pass


class PreconditionRequiredException(ClientErrorException):
    pass


class TooManyRequestsException(ClientErrorException):
    pass


class BadRequestException(ClientErrorException):
    pass


class UnauthorizedException(ClientErrorException):
    pass


class PaymentRequiredException(ClientErrorException):
    pass


class ForbiddenException(ClientErrorException):
    pass


class NotFoundException(ClientErrorException):
    pass


class MethodNotAllowedException(ClientErrorException):
    pass


class NotAcceptableException(ClientErrorException):
    pass


class ProxyAuthenticationRequiredException(ClientErrorException):
    pass


class RequestTimeoutException(ClientErrorException):
    pass


class ConflictException(ClientErrorException):
    pass


class GoneException(ClientErrorException):
    pass


class LengthRequiredException(ClientErrorException):
    pass


class PreconditionFailedException(ClientErrorException):
    pass


class PayloadTooLargeException(ClientErrorException):
    pass


class URITooLongException(ClientErrorException):
    pass


class UnsupportedMediaTypeException(ClientErrorException):
    pass


class RangeNotSatisfiableException(ClientErrorException):
    pass


class ExpectationFailedException(ClientErrorException):
    pass


class IAmATeapotException(ClientErrorException):
    pass


class MisdirectedRequestException(ClientErrorException):
    pass


class UnprocessableEntityException(ClientErrorException):
    pass


class LockedException(ClientErrorException):
    pass


class FailedDependencyException(ClientErrorException):
    pass


class UpgradeRequiredException(ClientErrorException):
    pass


class UnavailableForLegalReasonsException(ClientErrorException):
    pass


class RequestHeaderFieldsTooLargeException(ClientErrorException):
    pass


class InternalServerErrorException(ServerErrorException):
    pass


class NotImplementedException(ServerErrorException):
    pass


class BadGatewayException(ServerErrorException):
    pass


class ServiceUnavailableException(ServerErrorException):
    pass


class GatewayTimeoutException(ServerErrorException):
    pass


class HTTPVersionNotSupportedException(ServerErrorException):
    pass


class VariantAlsoNegotiatesException(ServerErrorException):
    pass


class InsufficientStorageException(ServerErrorException):
    pass


class LoopDetectedException(ServerErrorException):
    pass


class NotExtendedException(ServerErrorException):
    pass


class NetworkAuthenticationRequiredException(ServerErrorException):
    pass


class MethodFailureException(ClientErrorException):
    pass


class BlockedByWindowsParentalControlsException(ClientErrorException):
    pass


class InvalidTokenException(ClientErrorException):
    pass


class TokenRequiredException(ClientErrorException):
    pass


class RequestHasBeenForbiddenByAntivirusException(ClientErrorException):
    pass


class BandwidthLimitExceededException(ServerErrorException):
    pass


class SiteIsFrozenException(ServerErrorException):
    pass


class LoginTimeoutException(ClientErrorException):
    pass


class RetryWithException(ClientErrorException):
    pass


class SSLCertificateErrorException(ClientErrorException):
    pass


class SSLCertificateRequiredException(ClientErrorException):
    pass


class HTTPRequestSentToHTTPSPortException(ClientErrorException):
    pass


class NoResponseException(ClientErrorException):
    pass


class ClientClosedRequestException(ClientErrorException):
    pass


class InvalidSSLCertificateException(ServerErrorException):
    pass


class SSLHandshakeFailedException(ServerErrorException):
    pass


class ATimeoutOccurredException(ServerErrorException):
    pass


class OriginIsUnreachableException(ServerErrorException):
    pass


class ConnectionTimedOutException(ServerErrorException):
    pass


class WebServerIsDownException(ServerErrorException):
    pass


class UnknownErrorException(ServerErrorException):
    pass
