# Generated by Django 3.2.3 on 2021-05-26 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_instractor_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user',
            new_name='student',
        ),
    ]