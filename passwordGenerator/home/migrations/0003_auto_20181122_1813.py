# Generated by Django 2.1.3 on 2018-11-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='passwordGenerator',
            field=models.CharField(default=1985, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='website',
            field=models.CharField(default=1985, max_length=500),
            preserve_default=False,
        ),
    ]
