# Generated by Django 3.2.7 on 2021-10-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saas_account', '0009_trello'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trello',
            name='miro_updated_at',
        ),
        migrations.AddField(
            model_name='trello',
            name='trello_updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
