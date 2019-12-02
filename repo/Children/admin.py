from django.contrib import admin
from .models import Children


class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['parents_id', 'child_name', 'device_name']


admin.site.register(Children, ChildrenAdmin)
