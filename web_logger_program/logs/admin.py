from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from web_logger.admin import admin_site

from .models import App, Log, LogField

admin_site.register(App)
admin_site.register(Log)
admin_site.register(LogField)
admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)
