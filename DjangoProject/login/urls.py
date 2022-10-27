from django.contrib import admin
from django.urls import path , include
from .views import StudentView,TeacherView , UserRegistrationView, UserLoginView ,testview


urlpatterns = [
    path('', UserRegistrationView.as_view(), name = "RegistrationView"),
    path('login/', UserLoginView.as_view(), name = "LoginView"),
    path('student-dashboard/', StudentView, name = "StudentView"),
    path('Faculty-dashboard/', TeacherView, name = "TeacherView"),
    path('dashboard/', testview, name = "test"),
]