from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from core.models import Journalist, Source, Writer


class JournalistRegistrationSerializer(RegisterSerializer):
    journalist = serializers.PrimaryKeyRelatedField(
        read_only=True,)  # by default allow_null = False
    company = serializers.ForeignKey
    image
    bio
    created_at
    updated_at

    def get_cleaned_data(self):
        data = super(JournalistRegistrationSerializer, self).get_cleaned_data()

        return data

    def save(self, request):
        user = super(JournalistRegistrationSerializer, self).save(request)
        user.is_journalist = True
        user.save()
        journalist = Journalist(journalist=user)
        journalist.save()
        return user


class WriterRegistrationSerializer(RegisterSerializer):
    writer = serializers.PrimaryKeyRelatedField(
        read_only=True,)  # by default allow_null = False

    def get_cleaned_data(self):
        data = super(WriterRegistrationSerializer, self).get_cleaned_data()

        return data

    def save(self, request):
        user = super(WriterRegistrationSerializer, self).save(request)
        user.is_writer = True
        user.save()
        writer = Writer(writer=user)
        writer.save()
        return user


class SourceRegistrationSerializer(RegisterSerializer):
    source = serializers.PrimaryKeyRelatedField(
        read_only=True,)  # by default allow_null = False

    def get_cleaned_data(self):
        data = super(SourceRegistrationSerializer, self).get_cleaned_data()

        return data

    def save(self, request):
        user = super(SourceRegistrationSerializer, self).save(request)
        user.is_writer = True
        user.save()
        source = Source(source=user)
        source.save()
        return user
