# Generated by Django 3.1.1 on 2020-09-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='percent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='slider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
