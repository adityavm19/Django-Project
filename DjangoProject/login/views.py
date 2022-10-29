from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import UserRegistrationSerializer , UserLoginSerializer
from django.contrib.auth import authenticate
from django.urls import reverse
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from .models import User


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
class UserRegistrationView(generics.GenericAPIView):
    #renderer_classes = [UserRenderer]
    serializer_class = UserRegistrationSerializer
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'msg': 'Registration Successful',"User": serializer.data, 'token':token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class UserLoginViewNew(TokenObtainPairView):
    #renderer_classes = [UserRenderer]
    serializer_class = UserLoginSerializer




def StudentView(request):
    return HttpResponse("Student's PAGE123!!!")

def FacultyView(request):
    return HttpResponse("Faculty's PAGE!!!")

def testview(request):
    return HttpResponse("ITS A TEST!!!")