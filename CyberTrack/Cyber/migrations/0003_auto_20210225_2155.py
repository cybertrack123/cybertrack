# Generated by Django 3.0.4 on 2021-02-25 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cyber', '0002_history'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='History',
            new_name='Commment',
        ),
        migrations.RenameField(
            model_name='commment',
            old_name='History',
            new_name='Comment_Text',
        ),
    ]