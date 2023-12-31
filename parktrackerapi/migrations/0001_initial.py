# Generated by Django 4.1.3 on 2023-08-16 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park_name', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('park_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_name', models.CharField(max_length=50)),
                ('length', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('park_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parktrackerapi.park')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('uid', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrailComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parktrackerapi.user')),
                ('trail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parktrackerapi.trail')),
            ],
        ),
        migrations.AddField(
            model_name='trail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parktrackerapi.user'),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('site_type', models.CharField(max_length=50)),
                ('park_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parktrackerapi.park')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parktrackerapi.user')),
            ],
        ),
        migrations.AddField(
            model_name='park',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parktrackerapi.user'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parktrackerapi.park')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parktrackerapi.user')),
            ],
        ),
    ]
