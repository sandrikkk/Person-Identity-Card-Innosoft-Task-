# Generated by Django 4.1 on 2022-09-02 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sex',
            options={'verbose_name': 'sexs', 'verbose_name_plural': 'Sex'},
        ),
        migrations.AddField(
            model_name='department',
            name='department',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='person.department'),
        ),
    ]
