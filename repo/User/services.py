import jwt
from datetime import datetime, timedelta

from .models import User
from conf.settings import SECRET_KEY


class UserService(object):
    @staticmethod
    def check_id_exists(user_id: str) -> bool:
        return True if len(User.objects.filter(user_id=user_id).values()) else False

    @staticmethod
    def create_new_user(*user_data) -> None:
        User(user_id=user_data[0], user_pw=user_data[1], name=user_data[2], birth_date=user_data[3], sex=user_data[4]).save()

    @staticmethod
    def check_id_pw_match(user_id: str, user_pw: str) -> bool:
        return True if User.objects.get(user_id=user_id).user_pw == user_pw else False

    @staticmethod
    def get_pk_with_id(user_id: str) -> int:
        return User.objects.get(user_id=user_id).id


class JWTService(object):
    @staticmethod
    def create_jwt_with_pk(pk: int, expired_minute: int = 60) -> str:
        return jwt.encode({
            'id': pk,
            'exp': datetime.utcnow() + timedelta(seconds=60*expired_minute)
        }, SECRET_KEY, algorithm='HS256')
