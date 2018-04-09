# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_twitter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitterrecententries',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_twitter_twitterrecententries', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='twittersearch',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_twitter_twittersearch', serialize=False, to='cms.CMSPlugin'),
        ),
    ]
