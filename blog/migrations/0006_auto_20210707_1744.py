# Generated by Django 3.2 on 2021-07-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210706_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='status_garegory',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='artile',
            name='category',
            field=models.ManyToManyField(related_name='article', to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]
