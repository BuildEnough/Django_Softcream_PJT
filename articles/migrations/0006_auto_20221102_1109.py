# Generated by Django 3.2.13 on 2022-11-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20221102_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='image_1'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='image_2'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='image_3'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='image_4',
            field=models.ImageField(blank=True, upload_to='image_4'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='image_5',
            field=models.ImageField(blank=True, upload_to='image_5'),
        ),
    ]
