from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=100)
    user_pw = models.TextField()
    name = models.CharField(max_length=10)
    birth_date = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.user_id

