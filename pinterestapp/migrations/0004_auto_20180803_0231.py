# Generated by Django 2.0.5 on 2018-08-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterestapp', '0003_auto_20180802_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pin',
            name='board',
        ),
        migrations.AlterField(
            model_name='pin',
            name='photo',
            field=models.ImageField(upload_to='pins/'),
        ),
    ]
