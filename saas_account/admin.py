#

from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from saas_account.models import Client, Domain, Zoom, Slack, Miro, Trello


class DomainInline(admin.TabularInline):
    model = Domain


class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    inlines = [DomainInline]
    list_display = ('schema_name', 'name', 'paid_until')

    def has_add_permission(self, request):
        if request.tenant.schema_name == 'public':
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.tenant.schema_name == 'public':
            return True
        else:
            return False

    def has_view_permission(self, request, obj=None):
        if request.tenant.schema_name == 'public':
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.tenant.schema_name == 'public':
            return True
        else:
            return False

    def has_view_or_change_permission(self, request, obj=None):
        if request.tenant.schema_name == 'public':
            return True
        else:
            return False

    def has_module_permission(self, request):
        if request.tenant.schema_name == 'public':
            return True
        else:
            return False


class ZoomAdmin(admin.ModelAdmin):
    ordering = ('date', 'zoom_updated_at',)


class SlackAdmin(admin.ModelAdmin):
    ordering = ('date', 'date_created',)


class MiroAdmin(admin.ModelAdmin):
    ordering = ('date', 'miro_updated_at',)

class TrelloAdmin(admin.ModelAdmin):
    ordering = ('date', 'trello_updated_at',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Zoom, ZoomAdmin)
admin.site.register(Slack, SlackAdmin)
admin.site.register(Miro, MiroAdmin)
admin.site.register(Trello, TrelloAdmin)
