# Generated by Django 3.2.3 on 2021-06-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_order_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='price',
            new_name='offer_price',
        ),
        migrations.AddField(
            model_name='course',
            name='regular_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]