# Generated by Django 3.1.4 on 2021-01-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nirvata', '0010_auto_20210111_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryphoto',
            name='date',
            field=models.DateField(help_text='YYYY-DD-MM'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(help_text='YYYY-DD-MM'),
        ),
    ]