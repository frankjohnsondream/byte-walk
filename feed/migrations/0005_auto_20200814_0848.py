# Generated by Django 3.0.8 on 2020-08-14 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20200813_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=255),
        ),
    ]
