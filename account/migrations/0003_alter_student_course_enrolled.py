# Generated by Django 3.2.3 on 2021-05-18 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_enrolled',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
    ]
