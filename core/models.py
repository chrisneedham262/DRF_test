
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator, URLValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from company_api.models import Company


def upload_to(instance, filename):
    return 'users/{filename}'.format(filename=filename)


class User(AbstractUser):
    is_journalist = models.BooleanField(default=False)
    is_writer = models.BooleanField(default=False)
    is_source = models.BooleanField(default=False)


class Profile(models.Model):
    image = models.ImageField(_("Image"), null=True,
                              upload_to=upload_to, default='user/default.jpg')
    bio = models.TextField(unique=False, blank=True)
    company = models.ManyToManyField(Company)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Journalist(models.Model):
    journalist = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.journalist.username


class Writer(models.Model):
    writer = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.writer.username


class Source(models.Model):
    source = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.source.username
