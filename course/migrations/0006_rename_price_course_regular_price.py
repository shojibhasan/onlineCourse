# Generated by Django 3.2.3 on 2021-06-01 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_rename_regular_price_course_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='price',
            new_name='regular_price',
        ),
    ]
