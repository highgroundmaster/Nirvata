# Generated by Django 3.1.4 on 2021-01-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nirvata', '0008_auto_20210111_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.CharField(help_text='DayS Month YYYY, Ex: 9th December 2020', max_length=30, null=True),
        ),
    ]
