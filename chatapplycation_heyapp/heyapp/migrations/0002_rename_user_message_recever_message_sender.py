# Generated by Django 4.2.3 on 2023-08-25 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heyapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='recever',
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.CharField(default=0, max_length=1000000),
            preserve_default=False,
        ),
    ]
