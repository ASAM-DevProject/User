from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    ('fields Me', {'fields': ('phone', 'National_Code')}),
)

UserAdmin.list_display += ('phone','National_Code')

admin.site.register(User, UserAdmin)