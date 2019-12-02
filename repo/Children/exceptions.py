from rest_framework.exceptions import APIException


# decode 실패 jwt
class InappropriateJwt(APIException):
    status_code = 422
    default_detail = "inappropriate jwt"


# jwt 포함 X
class NoIncludeJwt(APIException):
    status_code = 401
    default_detail = "no include jwt in headers"


class ExpiredJwt(APIException):
    status_code = 403
    default_detail = "Access token is expired."
