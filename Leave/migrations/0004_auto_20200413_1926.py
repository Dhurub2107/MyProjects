# Generated by Django 3.0.4 on 2020-04-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leave', '0003_auto_20200413_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavedata',
            name='Contact',
            field=models.CharField(max_length=12),
        ),
    ]
