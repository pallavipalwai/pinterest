# Generated by Django 2.0.5 on 2018-08-06 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinterestapp', '0006_auto_20180806_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='user',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
    ]
