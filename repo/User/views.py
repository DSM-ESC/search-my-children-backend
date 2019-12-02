from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    SignUpSerializers,
    LoginSerializers
)
from .services import (
    UserService,
    JWTService
)
from .exceptions import (
    UserIdIsExist,
    PasswordIsNotMatch
)


class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.initial_data
        _user_id = data["user_id"]
        _user_pw = data["user_pw"]

        if UserService.check_id_exists(_user_id) and UserService.check_id_pw_match(_user_id, _user_pw):
            return Response({
                'access_token': JWTService.create_jwt_with_pk(UserService.get_pk_with_id(_user_id))
            }, status=status.HTTP_200_OK)

        raise PasswordIsNotMatch


class SignUpAPI(APIView):
    def post(self, request):
        serializer = SignUpSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.initial_data
        if UserService.check_id_exists(user_id=data["user_id"]):
            raise UserIdIsExist

        UserService.create_new_user(data["user_id"], data["user_pw"], data["name"], data["birth_date"], data["sex"])
        return Response(data, status=status.HTTP_200_OK)
