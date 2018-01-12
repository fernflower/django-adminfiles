# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='upload date')),
                ('upload', models.FileField(upload_to=b'adminfiles', verbose_name='file')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='slug')),
                ('description', models.CharField(max_length=200, verbose_name='description', blank=True)),
                ('content_type', models.CharField(max_length=100, editable=False)),
                ('sub_type', models.CharField(max_length=100, editable=False)),
            ],
            options={
                'ordering': ['upload_date', 'title'],
                'verbose_name': 'file upload',
                'verbose_name_plural': 'file uploads',
            },
        ),
        migrations.CreateModel(
            name='FileUploadReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('upload', models.ForeignKey(to='adminfiles.FileUpload')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='fileuploadreference',
            unique_together=set([('upload', 'content_type', 'object_id')]),
        ),
    ]
