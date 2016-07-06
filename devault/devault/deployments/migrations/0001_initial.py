# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('environments', '0001_initial'),
        ('versions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='deployments_deployment_related_author', to=settings.AUTH_USER_MODEL, null=True)),
                ('editor', models.ForeignKey(related_name='deployments_deployment_related_editor', to=settings.AUTH_USER_MODEL, null=True)),
                ('environment', models.ForeignKey(to='environments.Environment')),
                ('version', models.ForeignKey(to='versions.Version')),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
                'get_latest_by': 'created',
            },
        ),
    ]
