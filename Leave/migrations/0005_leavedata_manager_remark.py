# Generated by Django 3.0.4 on 2020-04-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leave', '0004_auto_20200413_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavedata',
            name='Manager_Remark',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
