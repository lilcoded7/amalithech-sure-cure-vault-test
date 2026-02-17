from django.shortcuts import render
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class CreateUserAccount(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ["username", "email", "password"]

        def create(self, validated_data):
            password = validated_data.pop("password")
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user 
        
        def password(self, value):
            ...


class LoginUserAccountSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    user_id = serializers.UUIDField(read_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password
        )

        if not user:
            raise AuthenticationFailed('Invalid email or password')

        if not user.is_active:
            raise AuthenticationFailed('User account is disabled')

        refresh = RefreshToken.for_user(user)

        return {
            'email': user.email,
            'user_id': str(user.id),
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }
