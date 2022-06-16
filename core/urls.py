
from django.urls import path
from core.views import WriterRegistrationView, SourceRegistrationView, JournalistRegistrationView

app_name = "core"

urlpatterns = [
    path('registration/writer/', WriterRegistrationView.as_view(),
         name='register-writer'),
    path('registration/source/', SourceRegistrationView.as_view(),
         name='register-source'),
    path('registration/journalist/', JournalistRegistrationView.as_view(),
         name='register-journalist'),


]
