# Generated by Django 4.1 on 2022-09-02 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='images/')),
                ('cardnum', models.CharField(max_length=9, unique=True)),
                ('city', models.CharField(max_length=50)),
                ('personalid', models.CharField(max_length=11, unique=True)),
                ('dateofbirth', models.DateField()),
                ('dateofexpiry', models.DateField()),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.department')),
                ('sex', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.sex')),
            ],
        ),
    ]
