# Generated by Django 4.1.2 on 2023-02-11 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0004_alter_profile_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='profileimg',
        ),
    ]
