from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'name', 'birth_date', 'sex']


admin.site.register(User, UserAdmin)

