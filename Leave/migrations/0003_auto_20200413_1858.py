# Generated by Django 3.0.4 on 2020-04-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leave', '0002_remove_leavedata_app_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavedata',
            name='Contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='leavedata',
            name='Department',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='leavedata',
            name='Email',
            field=models.CharField(max_length=40),
        ),
    ]