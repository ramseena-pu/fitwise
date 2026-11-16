from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from newapp.serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
class UserCreateView(APIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            instance=User.objects.create_user(**cleaned_data)
            serializer_instance=UserSerializer(instance)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)