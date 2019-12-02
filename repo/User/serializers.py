from rest_framework import serializers


class SignUpSerializers(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    user_pw = serializers.CharField()
    name = serializers.CharField(max_length=10)
    birth_date = serializers.CharField(max_length=10)
    sex = serializers.CharField(max_length=10)


class LoginSerializers(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    user_pw = serializers.CharField(max_length=100)
