# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(verbose_name='内容')),
                ('time', models.TimeField(verbose_name='时间')),
            ],
            options={
                'verbose_name_plural': '作者',
                'verbose_name': '作者',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('sex', models.BooleanField(choices=[('m', '男'), ('f', '女')])),
            ],
            options={
                'verbose_name_plural': '作者',
                'verbose_name': '作者',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
            },
        ),
    ]
