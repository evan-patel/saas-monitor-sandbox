# Generated by Django 3.2.7 on 2021-10-20 12:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('saas_account', '0005_auto_20211009_0257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slack',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name=uuid.uuid4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(null=True)),
                ('date_updated', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('ok', 'ok'), ('active', 'active'), ('resolved', 'resolved'), ('scheduled', 'scheduled'), ('completed', 'completed'), ('cancelled', 'cancelled')], max_length=20)),
                ('active_incidents', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
