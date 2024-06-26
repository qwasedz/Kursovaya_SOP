# Generated by Django 5.0.3 on 2024-04-06 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('designer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_post', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5000)),
                ('photo_material_url', models.ImageField(null=True, upload_to='posts/img/')),
                ('video_material_url', models.FileField(null=True, upload_to='posts/video/')),
                ('date', models.DateField()),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designer.designer')),
            ],
        ),
    ]
