from .models import Children
from User.models import User


class ChildrenService(object):
    @staticmethod
    def create_new_children(pk: int, child_name: str, device_name: str) -> None:
        Children(parents_id=User.objects.get(pk=pk), child_name=child_name, device_name=device_name).save()
