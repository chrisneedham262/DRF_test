from django.db import models
from django.core.validators import RegexValidator, URLValidator
from django.utils.deconstruct import deconstructible
from core.models import Profile


@deconstructible
class RequireHttpOrHttpsUrl:
    def __call__(self, value):
        if not value.startswith("http://") and not value.startswith("https://"):
            raise ValidationError('Please provide a http or https resource')


class Company(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(
        verbose_name="URL",
        max_length=500, null=True,
        validators=[RequireHttpOrHttpsUrl()]
    )
    monthly_visitors = models.IntegerField(blank=True, null=True)
    domain_authority = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    about = models.TextField(unique=False, blank=True)
    staff = models.ManyToMany("core.Profile", related_name="staff")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
