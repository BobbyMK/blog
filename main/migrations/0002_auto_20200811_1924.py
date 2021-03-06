# Generated by Django 3.0.7 on 2020-08-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=80, verbose_name='Заголовок'),
        ),
    ]
