# Generated by Django 2.2.14 on 2022-07-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20220717_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='user1',
            name='paisa_DOB',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='user1',
            name='paisa_api_appname',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='user1',
            name='paisa_api_appsource',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='user1',
            name='paisa_api_encryptkey',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='user1',
            name='paisa_api_password',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='user1',
            name='paisa_api_userid',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='user1',
            name='paisa_api_userkey',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='user1',
            name='paisa_email',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='user1',
            name='paisa_password',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='user1',
            name='passphrase',
            field=models.CharField(default='TYRFBYNWDjnXDHwmaUGv', max_length=50),
        ),
    ]
