from django.contrib import admin
from .models import ArSystems,ArBooks,ArDeliveries,ArRoleOptions,ArRoles,ArStatus,ArSystemOptions,ArUserRoles,ArUsers

admin.site.register(ArSystems)
admin.site.register(ArBooks)
admin.site.register(ArDeliveries)
admin.site.register(ArRoleOptions)
admin.site.register(ArRoles)
admin.site.register(ArStatus)
admin.site.register(ArSystemOptions)
admin.site.register(ArUserRoles)
admin.site.register(ArUsers)