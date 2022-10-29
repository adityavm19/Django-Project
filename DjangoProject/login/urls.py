from django.contrib import admin
from django.urls import path , include
from .views import StudentView,FacultyView , UserRegistrationView,testview, UserLoginViewNew
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = "RegistrationView"),
    path('login/', UserLoginViewNew.as_view(), name = "LoginView"),
    path('refresh-token/', TokenRefreshView.as_view(), name = "RefreshToken"),
    path('student-dashboard/', StudentView, name = "StudentView"),
    path('Faculty-dashboard/', FacultyView, name = "FacultyView"),
    path('dashboard/', testview, name = "test"),
]