# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-10-07 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('author', models.CharField(default='admin', max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_gallery.Category')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_gallery.Location'),
        ),
    ]
