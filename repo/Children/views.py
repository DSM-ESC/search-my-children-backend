import jwt

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from User.services import JWTService
from .exceptions import (
    NoIncludeJwt,
    InappropriateJwt,
    ExpiredJwt
)
from .services import (
    ChildrenService
)


class ChildrenHandler(APIView):
    def post(self, request):
        try:
            _id = JWTService.decode_jwt_to_pk(request.headers['Authorization'])
        except KeyError:
            raise NoIncludeJwt
        except jwt.exceptions.DecodeError:
            raise InappropriateJwt
        except jwt.exceptions.ExpiredSignatureError:
            raise ExpiredJwt

        data = request.data
        item_list = list(data.items())

        if not 0 < len(item_list) <= 5 or not data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        for item in item_list:
            ChildrenService.create_new_children(_id, item[0], item[1])

        return Response(_id, status=status.HTTP_200_OK)
