# Generated by Django 4.0 on 2022-01-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0003_alter_tasks_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]