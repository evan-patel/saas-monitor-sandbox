from django import forms
from django.conf import settings
from django.core.validators import RegexValidator
from django_tenants.utils import schema_context

from accounts.models import User


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    site_name = forms.CharField(validators=[RegexValidator(
        regex='^[a-z0-9_-]*$',
        message='Invalid Site Name, Site Name should only contain small letters,underscores(_) and dash(-)',
        code='invalid_site_name'
    )], widget=forms.TextInput(attrs={'class': 'form-control w-auto d-inline-block'}), required=True)

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        email = self.cleaned_data.get('email')
        with schema_context(settings.PUBLIC_SCHEMA_NAME):
            user = User.objects.filter(email=email)
            if user.exists():
                self.add_error('email', "Email Already Exist")
