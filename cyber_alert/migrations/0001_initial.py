# Generated by Django 2.0.5 on 2018-11-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phoneno', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GiverTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('aadharno', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('mobileno', models.CharField(max_length=50)),
                ('bankname', models.CharField(max_length=50)),
                ('accountno', models.CharField(max_length=50)),
                ('branchname', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('ifsccode', models.CharField(max_length=50)),
                ('micrcode', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('transationid', models.CharField(max_length=50)),
                ('userid', models.ForeignKey(on_delete=models.CASCADE, to='cyber_alert.AdminRegister')),
            ],
        ),
    ]
