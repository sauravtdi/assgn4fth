from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .templates.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import Group
from user.models import ActivityPeriod
# Register your models here.
User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'admin',)
    list_filter = ('admin', 'staff', 'active',)
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password', 'timezone')}),
        ('Permissions', {'fields': ('admin', 'staff',
                                    'active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'timezone', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(ActivityPeriod)
admin.site.unregister(Group)
