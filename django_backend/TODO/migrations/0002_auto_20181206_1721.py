# Generated by Django 2.1.4 on 2018-12-06 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='decription',
            new_name='description',
        ),
    ]
