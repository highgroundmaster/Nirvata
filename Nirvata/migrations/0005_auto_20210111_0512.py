# Generated by Django 3.1.4 on 2021-01-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nirvata', '0004_auto_20210111_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryphoto',
            name='date',
            field=models.CharField(help_text='Day Mon YYYY, Ex: 9th Dec 2020', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='galleryphoto',
            name='description',
            field=models.TextField(help_text='Upper Limit : 150 characters', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='galleryphoto',
            name='image',
            field=models.CharField(help_text='Pass the url here', max_length=1000, null=True),
        ),
    ]
