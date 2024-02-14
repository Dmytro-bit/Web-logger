from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from web_logger.admin import admin_site

from .models import Log, LogField, App
from .utils import password_encryption

admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)


class LogFieldInline(admin.TabularInline):
    model = LogField
    fields = ('log_name', 'log_value')
    extra = 0


class LogInline(admin.TabularInline):
    model = Log
    readonly_fields = ('timestamp',)
    extra = 0


class AdminApp(admin.ModelAdmin):
    list_display = ('name', 'key', 'active')
    inlines = [LogInline]

    def save_model(self, request, obj, form, change):
        obj.key = password_encryption(obj.key)
        super().save_model(request, obj, form, change)


class AdminLog(admin.ModelAdmin):
    list_display = ('level', 'app', 'timestamp')
    inlines = [LogFieldInline]


admin_site.register(Log, AdminLog)
admin_site.register(App, AdminApp)
admin_site.register(LogField)
