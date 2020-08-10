# Generated by Django 3.0.4 on 2020-04-13 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Department_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('Manager_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Manager_Name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField(auto_created=True, unique=True)),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.CharField(default=None, max_length=40)),
                ('Contact', models.IntegerField(default=None)),
                ('From_Date', models.DateField()),
                ('To_Date', models.DateField()),
                ('Leave_Type', models.CharField(max_length=20)),
                ('Department', models.CharField(default=None, max_length=30)),
                ('Reason', models.CharField(max_length=200)),
                ('No_Days', models.IntegerField()),
                ('Apply_Date', models.DateField(auto_now=True)),
                ('Manager_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leave.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_name', models.CharField(max_length=20)),
                ('Emp_Prob', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=2)),
                ('Emp_ML', models.IntegerField()),
                ('Emp_CL', models.IntegerField()),
                ('Emp_CompOff', models.IntegerField()),
                ('Emp_Email', models.EmailField(default=None, max_length=50, unique=True)),
                ('Date', models.DateField(auto_now=True)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leave.Department')),
                ('Emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Leave.Manager')),
            ],
        ),
    ]
