from django.contrib import admin

from .models import polls
from .models import post

admin.site.register(polls)
admin.site.register(post)