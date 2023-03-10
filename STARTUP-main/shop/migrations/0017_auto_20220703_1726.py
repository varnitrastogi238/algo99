# Generated by Django 2.2.14 on 2022-07-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20220703_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradingview_orders',
            name='broker',
            field=models.CharField(default='NONE', max_length=20),
        ),
        migrations.AddField(
            model_name='user1',
            name='alpaca_api_keys',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='user1',
            name='alpaca_base_url',
            field=models.CharField(default='https://app.alpaca.markets', max_length=100),
        ),
        migrations.AddField(
            model_name='user1',
            name='alpaca_secret_keys',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='user1',
            name='passphrase',
            field=models.CharField(default='zNWoHkAdmnqyecVnaGHD', max_length=50),
        ),
    ]
