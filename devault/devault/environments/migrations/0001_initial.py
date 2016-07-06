# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('namemixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='users.NameMixIn')),
                ('comment', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('tier', models.IntegerField(choices=[(0, b'Development'), (1, b'Integration'), (2, b'Testing'), (3, b'Staging'), (4, b'Production')])),
                ('author', models.ForeignKey(related_name='environments_environment_related_author', to=settings.AUTH_USER_MODEL, null=True)),
                ('editor', models.ForeignKey(related_name='environments_environment_related_editor', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
                'get_latest_by': 'created',
            },
            bases=('users.namemixin', models.Model),
        ),
    ]
