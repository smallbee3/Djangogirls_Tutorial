# Generated by Django 2.0.1 on 2018-01-31 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='created_date',
        ),
    ]
