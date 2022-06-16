
from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from core.serializers import (
    JournalistRegistrationSerializer, SourceRegistrationSerializer, WriterRegistrationSerializer
)


class JournalistRegistrationView(RegisterView):
    serializer_class = JournalistRegistrationSerializer


class WriterRegistrationView(RegisterView):
    serializer_class = WriterRegistrationSerializer


class SourceRegistrationView(RegisterView):
    serializer_class = SourceRegistrationSerializer
