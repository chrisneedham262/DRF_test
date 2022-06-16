from django.contrib import admin

from core.models import Journalist, Source, Writer, User
admin.site.register(User)
admin.site.register(Journalist)
admin.site.register(Source)
admin.site.register(Writer)
