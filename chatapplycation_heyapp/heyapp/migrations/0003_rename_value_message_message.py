# Generated by Django 4.2.3 on 2023-08-26 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heyapp', '0002_rename_user_message_recever_message_sender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='value',
            new_name='message',
        ),
    ]
