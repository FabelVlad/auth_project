from django.contrib import admin

# Register your models here.
from apps.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
