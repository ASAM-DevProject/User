# Generated by Django 3.1.3 on 2021-05-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210516_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='National_Code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
