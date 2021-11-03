from django.conf import settings
from django.shortcuts import render

from accounts.models import User
from saas_account.forms import RegistrationForm
from saas_account.models import Zoom, Slack, Miro, Trello
from saas_account.utils import create_tenant_and_create_super_user


def register_tenant(request):
    context = dict()
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(request.POST, request.body)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = User.objects.create_user(
                first_name=clean_data.get('first_name'),
                last_name=clean_data.get('last_name'),
                username=clean_data.get('email').split('@')[0],
                email=clean_data.get('email'),
                password=clean_data.get('password')
            )
            user_dict = {
                "email": user.email,
                "username": user.username,
                "password": clean_data.get('password'),
                "first_name": clean_data.get('first_name'),
                "last_name": clean_data.get('last_name')
            }
            create_tenant_and_create_super_user(schema_name=user.display_name.replace(' ', ''),
                                                name=user.display_name,
                                                site_name=clean_data.get('site_name'),
                                                user_dict=user_dict
                                                )
            context['success'] = True
    context['form'] = form
    context['SITE_HOST'] = settings.SITE_HOST
    return render(request, 'registration/signup.html', context=context)


def view_status_for_services(request):
    """
    Renders Index page with Zoom data
    """
    context = dict()
    zoom = Zoom.objects.all().order_by('-date')
    slack = Slack.objects.all().order_by('-date')
    miro = Miro.objects.all().order_by('-date')
    trello = Trello.objects.all().order_by('-date')
    context['zoom'] = zoom[0:11]
    context['zoom_current'] = zoom.first()
    context['slack'] = slack[0:11]
    context['slack_current'] = slack.first()
    context['miro'] = miro[0:11]
    context['miro_current'] = miro.first()
    context['trello'] = trello[0:11]
    context['trello_current'] = trello.first()

    return render(request, 'index.html', context=context)
