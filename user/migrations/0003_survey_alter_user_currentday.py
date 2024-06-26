# Generated by Django 4.2.13 on 2024-05-24 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_courseday_user_currentday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField()),
                ('enoughSleep', models.IntegerField()),
                ('tiredness', models.IntegerField()),
                ('quality', models.IntegerField()),
                ('fallingAspleep', models.IntegerField()),
                ('nightWaking', models.IntegerField()),
                ('electronicDevices', models.IntegerField()),
                ('routine', models.IntegerField()),
                ('caffeine', models.IntegerField()),
                ('refreshed', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='currentDay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.courseday'),
        ),
    ]
