# Generated by Django 2.2 on 2019-05-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20190529_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pic',
            field=models.ImageField(blank=True, default='images.png', upload_to=''),
        ),
    ]
