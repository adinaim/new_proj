from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import logging

from .serializers import (
    RegistrationSerializer,
    ActivationSerializer,
)


class RegistrationView(APIView):
    def post(self, request: Request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
            'Thanks for registration. Activate your account.',
            status=status.HTTP_201_CREATED
            )


class ActivationView(APIView):
    def post(self, request: Request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate_account()
            return Response('Аккаунт активрован',
            status=status.HTTP_200_OK)
        