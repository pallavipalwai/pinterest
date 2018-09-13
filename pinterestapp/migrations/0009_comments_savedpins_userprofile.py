# Generated by Django 2.0.5 on 2018-08-06 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pinterestapp', '0008_auto_20180806_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=256)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('commented_pin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterestapp.Pin')),
            ],
        ),
        migrations.CreateModel(
            name='SavedPins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterestapp.Pin')),
                ('savedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savedby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=20)),
                ('lastname', models.CharField(blank=True, max_length=20)),
                ('profile_picture', models.ImageField(blank=True, default='imageplaceholder.jpg', upload_to='profilepictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
