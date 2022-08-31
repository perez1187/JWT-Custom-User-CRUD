from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin): # he also write _UserAdmin
    list_display= (
        "id",
        "email",
        "first_name",
        "last_name"
    )

admin.site.register(models.User, UserAdmin)
