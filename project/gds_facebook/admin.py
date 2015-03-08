from django.contrib import admin
from django.db import models

from .models import FacebookAccessToken
from .forms import FacebookAccessInput


@admin.register(FacebookAccessToken)
class FacebookAccessAdmin(admin.ModelAdmin):
    list_display = ('short_token', 'is_valid',)
    formfield_overrides = {
        models.CharField: {'widget': FacebookAccessInput},
    }


