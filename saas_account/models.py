from django.conf import settings
from django.db import models
from django.utils import timezone
from django_tenants.models import TenantMixin, DomainMixin
from django_tenants.utils import get_tenant_domain_model

from SAAS_MONITOR.models import AbstractIdCreatedUpdatedModel
from saas_account.constants import SLACK_STATUS, INDICATORS


class Client(AbstractIdCreatedUpdatedModel, TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True

    def get_primary_domain(self):
        """
        Returns the primary domain of the tenant
        """

        try:
            domain = self.domains
            return domain
        except get_tenant_domain_model().DoesNotExist:
            return None


class Domain(AbstractIdCreatedUpdatedModel, DomainMixin):
    tenant = models.OneToOneField(settings.TENANT_MODEL, db_index=True, related_name='domains',
                                  on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100, null=False, blank=True)

    def save(self, *args, **kwargs):
        self.domain = f"{self.site_name}.{settings.SITE_HOST}"
        super(Domain, self).save(*args, *kwargs)


class Zoom(AbstractIdCreatedUpdatedModel):
    """
    Table stores status for zoom
    """

    indicator = models.CharField(max_length=20, choices=INDICATORS, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    zoom_updated_at = models.DateTimeField(null=True, blank=False)
    date = models.DateField(default=timezone.now)


class Slack(AbstractIdCreatedUpdatedModel):
    """
    Table stores status for Slack
    """
    date_created = models.DateTimeField(null=True, blank=False)
    date_updated = models.DateTimeField(null=True, blank=False)
    status = models.CharField(max_length=20, choices=SLACK_STATUS, null=False, blank=False)
    active_incidents = models.JSONField(null=True, blank=True)
    date = models.DateField(default=timezone.now)


class Miro(AbstractIdCreatedUpdatedModel):
    """
    Table stores status for zoom
    """

    indicator = models.CharField(max_length=20, choices=INDICATORS, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    miro_updated_at = models.DateTimeField(null=True, blank=False)
    date = models.DateField(default=timezone.now)


class Trello(AbstractIdCreatedUpdatedModel):
    """
    Table stores status for zoom
    """

    indicator = models.CharField(max_length=20, choices=INDICATORS, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    trello_updated_at = models.DateTimeField(null=True, blank=False)
    date = models.DateField(default=timezone.now)
