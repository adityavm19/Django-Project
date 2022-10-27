from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import UserRegistrationSerializer , UserLoginSerializer
from django.contrib.auth import authenticate
from django.urls import reverse
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request , format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'msg': 'Registration Successful', 'token':token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request , format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            acctype = serializer.data.get('accType')
            user = authenticate(email=email, password=password)
            if user is not None:
                get_tokens_for_user(user)
                if user.accType =="STUDENT" or user.accType == "student":
                    print(acctype)
                    #return Response({'msg': 'Login Successful','token':token}, status=status.HTTP_200_OK)
                    return HttpResponseRedirect(redirect_to=reverse("StudentView"))
                elif user.accType =="FACULTY" or user.accType=="faculty":
                    print(acctype)
                    return HttpResponseRedirect(redirect_to=reverse("FacultyView"))
                elif user.accType =="STAFF" or user.accType=="staff":
                    print(acctype)
                    return HttpResponseRedirect(redirect_to=reverse("test"))
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password Incorrect']}}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



def StudentView(request):
    return HttpResponse("Student's PAGE123!!!")

def FacultyView(request):
    return HttpResponse("Faculty's PAGE!!!")

def testview(request):
    return HttpResponse("ITS A TEST!!!")