# Generated by Django 2.1.5 on 2019-02-19 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_max_wesbites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='max_wesbites',
            new_name='max_websites',
        ),
    ]