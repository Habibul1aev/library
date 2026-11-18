from django.urls import path
from account.views import Register, Login, Profile, Logout, VerifyOTPCode


urlpatterns = [
    path('register/', Register.as_view()),
    path('otp-verify/', VerifyOTPCode.as_view()),
    path('login/', Login.as_view()),
    path('profile/', Profile.as_view()),
    path('logout/', Logout.as_view())
]
