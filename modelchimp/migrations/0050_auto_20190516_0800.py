# Generated by Django 2.2 on 2019-05-16 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelchimp', '0049_auto_20190516_0759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiment',
            old_name='epoch_durations',
            new_name='durations',
        ),
        migrations.RenameField(
            model_name='experiment',
            old_name='evaluation_parameters',
            new_name='metrics',
        ),
        migrations.RenameField(
            model_name='experiment',
            old_name='model_parameters',
            new_name='parameters',
        ),
    ]
