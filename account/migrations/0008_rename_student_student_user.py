# Generated by Django 3.2.3 on 2021-05-26 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_student_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student',
            new_name='user',
        ),
    ]
