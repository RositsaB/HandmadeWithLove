from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from handmade.accounts.models import Profile

UserModel = get_user_model()


class HandmadeUserAdmin(UserAdmin):
    model = UserModel
    list_display = ('email', 'is_staff',)
    list_filter = ('email', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'groups', 'user_permissions')}),
    )

    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(UserModel, HandmadeUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
