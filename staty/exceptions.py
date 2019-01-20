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


# noinspection PyPep8Naming
from socket import timeout as SocketTimeout, gaierror as SocketNameResolutionError, herror as SocketHostError
from .codes import *  # NOQA


# Base Exceptions & Mixins
# ========================


class StatyBaseException(Exception):
    pass


class RecoverableErrorMixin(Exception):
    pass


class UnrecoverableErrorMixin(Exception):
    pass


class RegistrationException(StatyBaseException):
    pass


class MissingHandlerException(StatyBaseException):
    pass


class HTTPError(StatyBaseException):
    status = None

    def __init__(self, *args, response=None, request=None):
        self.response = response
        self.request = request
        if self.request is None and self.response is not None:
            self.request = getattr(self.response, "request", None)
        super().__init__(*args)


# Connection Errors
# =================

class ConnectionException(StatyBaseException):
    pass


class ConnectionTimeoutException(SocketTimeout, ConnectionException, RecoverableErrorMixin):
    pass


class NameResolutionException(SocketNameResolutionError, ConnectionException, RecoverableErrorMixin):
    pass


class HostAddressException(SocketHostError, ConnectionException, RecoverableErrorMixin):
    pass


class SSLException(ConnectionException, RecoverableErrorMixin):
    pass


class ProxyException(ConnectionException, RecoverableErrorMixin):
    pass


# HTTP Client Errors
# ==================

class ClientErrorException(HTTPError):
    pass


class RecoverableClientErrorException(ClientErrorException, RecoverableErrorMixin):
    pass


class UnrecoverableClientErrorException(ClientErrorException, UnrecoverableErrorMixin):
    pass


class PreconditionRequiredException(UnrecoverableClientErrorException):
    status = PreconditionRequired()


class TooManyRequestsException(RecoverableClientErrorException):
    status = TooManyRequests()


class BadRequestException(UnrecoverableClientErrorException):
    status = BadRequest()


class UnauthorizedException(UnrecoverableClientErrorException):
    status = Unauthorized()


class PaymentRequiredException(UnrecoverableClientErrorException):
    status = PaymentRequired()


class ForbiddenException(UnrecoverableClientErrorException):
    status = Forbidden()


class NotFoundException(UnrecoverableClientErrorException):
    status = NotFound()


class MethodNotAllowedException(UnrecoverableClientErrorException):
    status = MethodNotAllowed()


class NotAcceptableException(UnrecoverableClientErrorException):
    status = NotAcceptable()


class ProxyAuthenticationRequiredException(UnrecoverableClientErrorException):
    status = ProxyAuthenticationRequired()


class RequestTimeoutException(RecoverableClientErrorException):
    status = RequestTimeout()


class ConflictException(UnrecoverableClientErrorException):
    status = Conflict()


class GoneException(UnrecoverableClientErrorException):
    status = Gone()


class LengthRequiredException(UnrecoverableClientErrorException):
    status = LengthRequired()


class PreconditionFailedException(UnrecoverableClientErrorException):
    status = PreconditionFailed()


class PayloadTooLargeException(UnrecoverableClientErrorException):
    status = PayloadTooLarge()


class URITooLongException(UnrecoverableClientErrorException):
    status = URITooLong()


class UnsupportedMediaTypeException(UnrecoverableClientErrorException):
    status = UnsupportedMediaType()


class RangeNotSatisfiableException(UnrecoverableClientErrorException):
    status = RangeNotSatisfiable()


class ExpectationFailedException(UnrecoverableClientErrorException):
    status = ExpectationFailed()


class IAmATeapotException(UnrecoverableClientErrorException):
    status = IAmATeapot()


class MisdirectedRequestException(UnrecoverableClientErrorException):
    status = MisdirectedRequest()


class UnprocessableEntityException(UnrecoverableClientErrorException):
    status = UnprocessableEntity()


class LockedException(UnrecoverableClientErrorException):
    status = Locked()


class FailedDependencyException(UnrecoverableClientErrorException):
    status = FailedDependency()


class UpgradeRequiredException(UnrecoverableClientErrorException):
    status = UpgradeRequired()


class UnavailableForLegalReasonsException(UnrecoverableClientErrorException):
    status = UnavailableForLegalReasons()


class RequestHeaderFieldsTooLargeException(UnrecoverableClientErrorException):
    status = RequestHeaderFieldsTooLarge()


class MethodFailureException(UnrecoverableClientErrorException):
    status = MethodFailure()


class BlockedByWindowsParentalControlsException(UnrecoverableClientErrorException):
    status = BlockedByWindowsParentalControls()


class InvalidTokenException(UnrecoverableClientErrorException):
    status = InvalidToken()


class TokenRequiredException(UnrecoverableClientErrorException):
    status = TokenRequired()


class RequestHasBeenForbiddenByAntivirusException(UnrecoverableClientErrorException):
    status = RequestHasBeenForbiddenByAntivirus()


class LoginTimeoutException(RecoverableClientErrorException):
    status = LoginTimeout()


class RetryWithException(RecoverableClientErrorException):
    status = RetryWith()


class SSLCertificateErrorException(UnrecoverableClientErrorException):
    status = SSLCertificateError()


class SSLCertificateRequiredException(UnrecoverableClientErrorException):
    status = SSLCertificateRequired()


class HTTPRequestSentToHTTPSPortException(UnrecoverableClientErrorException):
    status = HTTPRequestSentToHTTPSPort()


class NoResponseException(UnrecoverableClientErrorException):
    status = NoResponse()


class ClientClosedRequestException(RecoverableClientErrorException):
    status = ClientClosedRequest()


# HTTP Server Errors
# ==================

class ServerErrorException(HTTPError, RecoverableErrorMixin):
    pass


class InternalServerErrorException(ServerErrorException):
    status = InternalServerError


class NotImplementedException(ServerErrorException):
    status = NotImplemented()


class BadGatewayException(ServerErrorException):
    status = BadGateway()


class ServiceUnavailableException(ServerErrorException):
    status = ServiceUnavailable()


class GatewayTimeoutException(ServerErrorException):
    status = GatewayTimeout()


class HTTPVersionNotSupportedException(ServerErrorException):
    status = HTTPVersionNotSupported()


class VariantAlsoNegotiatesException(ServerErrorException):
    status = VariantAlsoNegotiates()


class InsufficientStorageException(ServerErrorException):
    status = InsufficientStorage()


class LoopDetectedException(ServerErrorException):
    status = LoopDetected()


class NotExtendedException(ServerErrorException):
    status = NotExtended()


class NetworkAuthenticationRequiredException(ServerErrorException):
    status = NetworkAuthenticationRequired()


class BandwidthLimitExceededException(ServerErrorException):
    status = BandwidthLimitExceeded()


class SiteIsFrozenException(ServerErrorException):
    status = SiteIsFrozen()


class InvalidSSLCertificateException(ServerErrorException):
    status = InvalidSSLCertificate()


class SSLHandshakeFailedException(ServerErrorException):
    status = SSLHandshakeFailed()


class ATimeoutOccurredException(ServerErrorException):
    status = ATimeoutOccurred()


class OriginIsUnreachableException(ServerErrorException):
    status = OriginIsUnreachable()


class ConnectionTimedOutException(ServerErrorException):
    status = ConnectionTimedOut()


class WebServerIsDownException(ServerErrorException):
    status = WebServerIsDown()


class UnknownErrorException(ServerErrorException):
    status = UnknownError()
