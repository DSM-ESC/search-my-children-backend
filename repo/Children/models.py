from django.db import models
from User.models import User


class Children(models.Model):
    parents_id = models.ForeignKey(User, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
