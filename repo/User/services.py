from .models import User


class UserService(object):
    @staticmethod
    def check_id_exists(user_id: str) -> bool:
        return True if len(User.objects.filter(user_id=user_id).values()) else False
