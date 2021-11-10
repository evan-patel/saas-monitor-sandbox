import logging

import requests
from django.conf import settings
from django.utils import timezone
from django_tenants.utils import schema_context
from zappa.asynchronous import task


# Task run the code asynchronously on different lambda instance/


@task(remote_aws_lambda_function_name=settings.FUNCTION_NAME)
def create_tenant_and_create_super_user(schema_name, name, site_name, user_dict):
    """
    Creates client(tenant)
    and assign him a domain on registration
    """
    from saas_account.models import Client, Domain
    from accounts.models import User
    from django.core.mail import send_mail
    tenant = Client(schema_name=schema_name,
                    name=name,
                    paid_until='2030-12-12',
                    on_trial=False)
    tenant.save()
    domain = Domain()
    domain.domain = f"{site_name}.{settings.SITE_HOST}"
    domain.site_name = site_name
    domain.tenant = tenant
    domain.is_primary = True
    domain.save()

    with schema_context(f'{tenant.schema_name}'):
        User.objects.create_superuser(**user_dict)

    if not settings.SKIP_EMAIL:
        send_mail('Your Tenant is Read to access',
                  f'You can access you tenant on \n Link :- https://{site_name}.{settings.SITE_HOST} \n Username :- {user_dict.get("username")}',
                  f'{settings.DEFAULT_FROM_EMAIL}', [user_dict.get('email')], fail_silently=False)


def convert_time_to_time_zone(date_time):
    """
    Converts ISO-8062 datetime format to datetime python object
    :return: datetime
    """
    from dateutil.parser import isoparse
    # from dateutil import tz
    d = isoparse(date_time)
    # d.astimezone(tz.gettz(time_zone))
    return d


def get_zoom_status():
    """
    Collects data forr status from zoom api and store the data on db.
    """
    from saas_account.models import Zoom
    URL = 'https://status.zoom.us/api/v2/status.json'
    data = requests.get(url=URL)
    if data.status_code == 200:
        data_json = data.json()
        page = data_json.get("page")
        updated_at = convert_time_to_time_zone(page.get('updated_at'))
        zoom_status = data_json.get('status')
        zoom_status['zoom_updated_at'] = updated_at
        updated, created = Zoom.objects.update_or_create(zoom_updated_at=updated_at, date=timezone.now().date(),
                                                          defaults=zoom_status)
        logging.info(f"{str(updated)} -----> {created}")


def get_slack_status():
    from saas_account.models import Slack
    URL = 'https://status.slack.com/api/v2.0.0/current'
    data = requests.get(url=URL)
    if data.status_code == 200:
        data_json = data.json()
        date_created = data_json.get("date_created")
        date_updated = data_json.get("date_updated")
        active_incidents = data_json.get("active_incidents")
        status = data_json.get("status")
        defaults = {
            "date_updated": date_updated,
            "status": status,
            "active_incidents": active_incidents,
        }
        Slack.objects.update_or_create(date_created=date_created,defaults=defaults)
        logging.info(f"{str(updated)} -----> {created}")


def get_miro_status():
    from saas_account.models import Miro
    URL = 'https://status.miro.com/api/v2/status.json'
    data = requests.get(url=URL)
    if data.status_code == 200:
        data_json = data.json()
        page = data_json.get("page")
        updated_at = convert_time_to_time_zone(page.get('updated_at'))
        miro_status = data_json.get('status')
        miro_status['miro_updated_at'] = updated_at
        updated, created = Miro.objects.update_or_create(miro_updated_at=updated_at, date=timezone.now().date(),
                                                          defaults=miro_status)
        logging.info(f"{str(updated)} -----> {created}")


def get_trello_status():
    from saas_account.models import Trello
    URL = 'https://trello.status.atlassian.com/api/v2/status.json'
    data = requests.get(url=URL)
    if data.status_code == 200:
        data_json = data.json()
        page = data_json.get("page")
        updated_at = convert_time_to_time_zone(page.get('updated_at'))
        trello_status = data_json.get('status')
        trello_status['trello_updated_at'] = updated_at
        updated, created = Trello.objects.update_or_create(trello_updated_at=updated_at, date=timezone.now().date(),
                                                          defaults=trello_status)
        logging.info(f"{str(updated)} -----> {created}")
