# Generated by Django 3.2.7 on 2021-10-08 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saas_account', '0004_zoom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zoom',
            name='zoom_uppdated_at',
        ),
        migrations.AddField(
            model_name='zoom',
            name='zoom_updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
