from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    SignUpSerializers
)
from .services import (
    UserService
)
from .exceptions import (
    UserIdIsExist
)


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
