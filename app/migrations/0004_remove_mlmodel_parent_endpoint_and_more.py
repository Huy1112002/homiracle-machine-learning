# Generated by Django 5.0.6 on 2024-05-26 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_endpoint_mlmodel_mlmodelstatus_mlrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mlmodel',
            name='parent_endpoint',
        ),
        migrations.RemoveField(
            model_name='mlrequest',
            name='parent_mlmodel',
        ),
        migrations.RemoveField(
            model_name='mlmodelstatus',
            name='parent_mlmodel',
        ),
        migrations.DeleteModel(
            name='Endpoint',
        ),
        migrations.DeleteModel(
            name='MLRequest',
        ),
        migrations.DeleteModel(
            name='MLModel',
        ),
        migrations.DeleteModel(
            name='MLModelStatus',
        ),
    ]
