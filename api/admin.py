from django.contrib import admin
from .models import Task, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('name', 'mobile')}),
    )

admin.site.register(Task)