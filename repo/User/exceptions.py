from rest_framework.exceptions import APIException


class UserIdIsExist(APIException):
    status_code = 471
    default_detail = "This id is already exists."


class PasswordIsNotMatch(APIException):
    status_code = 470
    default_detail = "Id and password are not match."
