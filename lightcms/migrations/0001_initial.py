# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-12 05:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lightcms.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('order', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(choices=[('PAGE', 'Page')], default='PAGE', max_length=25)),
                ('publish', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISH', 'Publish')], default='DRAFT', max_length=25)),
                ('slug', lightcms.fields.SlugField(field='title')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lightcms_page_author', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lightcms_page_last_modified_by', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lightcms.Page', verbose_name='Parent Page')),
            ],
        ),
    ]
