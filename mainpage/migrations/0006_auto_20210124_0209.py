# Generated by Django 3.1.5 on 2021-01-23 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_auto_20210124_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_ewaste',
            name='Mob_number',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='add_ewaste',
            name='Ward',
            field=models.PositiveIntegerField(),
        ),
    ]
