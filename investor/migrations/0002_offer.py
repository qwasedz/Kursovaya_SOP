# Generated by Django 5.0.3 on 2024-04-22 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designer', '0001_initial'),
        ('investor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_offer', models.TextField(max_length=3000)),
                ('status', models.CharField(choices=[('0', 'Ожидание'), ('1', 'Доступно'), ('2', 'Отмена')], default='0', max_length=20)),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designer.designer')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investor.investor')),
            ],
        ),
    ]
