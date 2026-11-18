from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from account.models import User, OTPCode
from account.serializer import RegisterSerializer, LoginSerializer, ProfileSerializer, VerifyOTPCodeSerializer
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated
import random
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        email = serializer.validated_data['email']

        code = random.randint(100000, 999999)

        OTPCode.objects.filter(email=email).delete()
        OTPCode.objects.create(email=email, code=code)  

        send_mail(
            subject='Код от library',
            message=f'Ващ код {code}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[email]
        )


        return Response({'message': "Код отправен"})


class VerifyOTPCode(APIView):
    def post(self, request):
        serializer = VerifyOTPCodeSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            phone = serializer.validated_data['phone']
            otp = serializer.validated_data['otp']

            user = User.objects.create_user(
                email=email,
                username='Anonymus',
                password=password,
                phone=phone
            )

            otp.delete()

            token, created = Token.objects.get_or_create(user=user)

            return Response({'message': 'Seccsses account', 'token': token.key})

        return Response(serializer.errors)







class Login(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)
        login(request, user)

        return Response({
            'message': 'Login successful',
            'token': token.key
        })


class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)


class Logout(APIView):
    def post(self, request):
        Token.objects.get(user=request.user).delete()

        return Response({'message': 'Logout successful'})