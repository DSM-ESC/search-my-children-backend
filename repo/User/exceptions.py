from rest_framework.exceptions import APIException


class UserIdIsExist(APIException):
    status_code = 470
    default_detail = "This id is already exists."
