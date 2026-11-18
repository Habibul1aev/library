from rest_framework import serializers
from account.models import User, OTPCode
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'email']


class VerifyOTPCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    code = serializers.CharField(max_length=6)
    phone = serializers.CharField()

    def validate(self, attrs):
        email = attrs['email']
        code = attrs['code']

        otp = OTPCode.objects.filter(email=email, code=code).first()

        if not otp:
            raise serializers.ValidationError({'messages': 'Такой код нет'})

        if otp.is_expired():
             raise serializers.ValidationError({'messages': 'Код истек'})

        attrs['otp'] = otp

        return attrs



class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):

        user = authenticate(
            phone=attrs['phone'],
            password=attrs['password']
        )

        if user is None:
            raise serializers.ValidationError(
                'Неверный username или пароль'
            )

        attrs['user'] = user

        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'phone',
            'email',
        ]
        read_only_fields = ['id', 'username']