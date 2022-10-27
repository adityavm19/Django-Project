from django.contrib import admin
from django.urls import path , include
from .views import StudentView,FacultyView , UserRegistrationView, UserLoginView ,testview


urlpatterns = [
    path('', UserRegistrationView.as_view(), name = "RegistrationView"),
    path('login/', UserLoginView.as_view(), name = "LoginView"),
    path('student-dashboard/', StudentView, name = "StudentView"),
    path('Faculty-dashboard/', FacultyView, name = "FacultyView"),
    path('dashboard/', testview, name = "test"),
]