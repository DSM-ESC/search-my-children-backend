from .models import User


class UserService(object):
    @staticmethod
    def check_id_exists(user_id: str) -> bool:
        return True if len(User.objects.filter(user_id=user_id).values()) else False

    @staticmethod
    def create_new_user(*user_data) -> None:
        User(user_id=user_data[0], user_pw=user_data[1], name=user_data[2], birth_date=user_data[3], sex=user_data[4]).save()

    @staticmethod
    def check_id_pw_match(user_id: str, user_pw: str):
        return True if User.objects.get(user_id=user_id).user_pw == user_pw else False
